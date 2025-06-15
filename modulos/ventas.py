# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#       Funciones auxiliares
# ===============================

from controladores.date import conseguirDatoActual
from controladores.cupos import (
    restarCupoTPV,
    restarCupoTVS,
    consultarCuposTPV,
    consultarCuposTVS,
)
from types import SimpleNamespace


def convertirDatosVentas(respuesta):
    """
    Convierte la lista de tuplas resultado de la consulta en una lista
    de diccionarios con formato adecuado para las fechas, horas y tipos.
    """
    registros = []
    for registro in respuesta:
        fecha = registro[1]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = registro[2]
        hora = hora.strftime("%H:%M:%S")

        if registro[6]:
            codigo_de_viaje = registro[6]
            tipo = "Viaje Simple"
        else:
            codigo_de_viaje = registro[7]
            tipo = "Paquete de Viaje"
        dicConvertido = {
            "Id Venta": registro[0],
            "Fecha": fecha,
            "Hora": hora,
            "Medio de pago": registro[3],
            "Cuotas": registro[4],
            "Cantidad": registro[5],
            "Codigo de viaje": codigo_de_viaje,
            "Tipo": tipo,
            "Precio": registro[8],
        }
        registros.append(dicConvertido)

    return registros


# ===============================
#             CRUD
# ===============================


# ---- Crear nueva venta ----
def sumarVenta(data):
    """
    Inserta una nueva venta en la tabla ventas, con formato adecuado para fecha y hora.
    """
    res = conseguirDatoActual()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT MAX(vtas_id) FROM ventas")
        vtas_id = cur.fetchone()
        if vtas_id is None:
            vtas_id = 1
        else:
            vtas_id = int(vtas_id[0]) + 1

        cur.execute(
            "INSERT INTO ventas (vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                vtas_id,
                res["fecha"],
                res["hora"],
                data.data.medio_de_pago,
                data.data.cuotas,
                data.data.cantidad,
                data.data.codigo_vs,
                data.data.codigo_pv,
                data.data.precio,
            ),
        )

        cur.execute(
            "SELECT uc_id FROM usuario_comun WHERE correo_electronico = %s",
            (data.correo_electronico,),
        )
        uc_id = cur.fetchone()
        if uc_id is None:
            raise Exception("Usuario no encontrado")
        uc_id = int(uc_id[0])

        cur.execute(
            "INSERT INTO vtas_uc (vtas_id, uc_id) VALUES(%s,%s)", (vtas_id, uc_id)
        )

        if data.data.codigo_vs:
            # Consultar cupos es por si llegara a 0 y hay que marcarle no disponible
            restarCupoTVS(data.data.codigo_vs, data.data.cantidad)
            consultarCuposTVS(data.data.codigo_vs)

        else:
            # Consultar cupos es por si llegara a 0 y hay que marcarle no disponible
            restarCupoTPV(data.data.codigo_pv, data.data.cantidad)
            consultarCuposTPV(data.data.codigo_pv)
        conn.commit()

        return {"Mensaje": "Venta sumada"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Leer todas las ventas ----
def verVentas():
    """
    Recupera todas las ventas almacenadas y las convierte a formato legible.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM ventas")
        respuesta = cur.fetchall()
        nrespuesta = convertirDatosVentas(respuesta)

        return nrespuesta

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#          Consultas
# ===============================


# ---- Buscar venta por ID ----
def buscarVentaId(data):
    """
    Busca una venta por su ID y devuelve sus datos formateados.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM ventas WHERE vtas_id = %s", (data.vtas_id,))
        registro = cur.fetchall()
        fecha = registro[0][1]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = registro[0][2]
        hora = hora.strftime("%H:%M:%S")

        if registro[0][6]:
            codigo_de_viaje = registro[0][6]
            tipo = "Viaje Simple"
        else:
            codigo_de_viaje = registro[0][7]
            tipo = "Paquete de Viaje"

        dicConvertido = {
            "Id Venta": registro[0][0],
            "Fecha": fecha,
            "Hora": hora,
            "Medio de pago": registro[0][3],
            "Cuotas": registro[0][4],
            "Cantidad": registro[0][5],
            "Codigo de viaje": codigo_de_viaje,
            "Tipo": tipo,
            "Precio": registro[0][8],
        }

        return dicConvertido

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#         Cancelaciones
# ===============================


# ---- Cancelar compra de viaje simple ----
def cancelarCompraTVS(vtas_id):
    """
    Cancela una compra de viaje simple, actualiza cupos y elimina registros relacionados.
    """

    data = {"vtas_id": vtas_id}
    data = SimpleNamespace(**data)
    venta = buscarVentaId(data)

    if "error" in venta:
        raise Exception(venta["error"])

    cantidad = venta["Cantidad"]
    codigoViaje = venta["Codigo de viaje"]

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE viaje_simple SET cupos = cupos + %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        cur.execute("DELETE FROM vtas_uc WHERE vtas_id = %s", (vtas_id,))
        cur.execute("DELETE FROM ventas WHERE vtas_id = %s", (vtas_id,))

        conn.commit()

        consultarCuposTVS(codigoViaje)

        return {"Mensaje": "Compra cancelada"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Cancelar compra de paquete de viaje ----
def cancelarCompraTPV(vtas_id):
    """
    Cancela una compra de paquete de viaje, actualiza cupos y elimina registros relacionados.
    """

    data = {"vtas_id": vtas_id}
    data = SimpleNamespace(**data)
    venta = buscarVentaId(data)
    cantidad = venta["Cantidad"]
    codigoViaje = venta["Codigo de viaje"]

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE paquete_de_viajes SET cupos = cupos + %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        cur.execute("DELETE FROM vtas_uc WHERE vtas_id = %s", (vtas_id,))
        cur.execute("DELETE FROM ventas WHERE vtas_id = %s", (vtas_id,))

        conn.commit()

        consultarCuposTPV(codigoViaje)

        return {"Mensaje": "Compra cancelada"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
