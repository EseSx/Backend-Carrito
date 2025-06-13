# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import cursor

# ===============================
#       Funciones auxiliares
# ===============================


def convertirDatosVentas(respuesta):
    """
    Convierte la lista de tuplas resultado de la consulta en una lista
    de diccionarios con formato adecuado para las fechas, horas y tipos.
    """
    registros = []
    for registro in respuesta:
        dicConvertido = []
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
        dicConvertido.append(
            {
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
        )
        registros.append(dicConvertido)

    return registros


# ===============================
#             CRUD
# ===============================

from controladores.date import convertirDate, convertirHora


# ---- Crear nueva venta ----
def sumarVenta(data):
    """
    Inserta una nueva venta en la tabla ventas, con formato adecuado para fecha y hora.
    """
    fecha = convertirDate(data.fecha)
    hora = convertirHora(data.hora)

    cursor.execute(
        "INSERT INTO ventas (fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            fecha,
            hora,
            data.medio_de_pago,
            data.cuotas,
            data.cantidad,
            data.codigo_vs,
            data.codigo_pv,
            data.precio,
        ),
    )
    cursor.commit()

    return {"Mensaje": "Venta sumada"}


# ---- Leer todas las ventas ----
def verVentas():
    """
    Recupera todas las ventas almacenadas y las convierte a formato legible.
    """
    cursor.execute("SELECT * FROM ventas")
    respuesta = cursor.fetchall()
    nrespuesta = convertirDatosVentas(respuesta)

    return nrespuesta


# ===============================
#          Consultas
# ===============================


# ---- Buscar venta por ID ----
def buscarVentaId(vtas_id):
    """
    Busca una venta por su ID y devuelve sus datos formateados.
    """
    cursor.execute("SELECT * FROM ventas WHERE vtas_id = %s", (vtas_id,))
    registro = cursor.fetchall()
    dicConvertido = []
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

    dicConvertido.append(
        {
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
    )

    return dicConvertido


# ===============================
#         Cancelaciones
# ===============================


# ---- Cancelar compra de viaje simple ----
def cancelarCompraTVS(vtas_id):
    """
    Cancela una compra de viaje simple, actualiza cupos y elimina registros relacionados.
    """
    venta = buscarVentaId(vtas_id)
    cantidad = venta[0]["Cantidad"]
    codigoViaje = venta[0]["Codigo de viaje"]

    cursor.execute(
        "UPDATE viaje_simple SET cupos = cupos + %s WHERE codigo = %s",
        (cantidad, codigoViaje),
    )
    cursor.execute("DELETE FROM vtas_uc WHERE vtas_id = %s", (vtas_id,))
    cursor.execute("DELETE FROM ventas WHERE vtas_id = %s", (vtas_id,))

    cursor.commit()

    return {"Mensaje": "Compra cancelada"}


# ---- Cancelar compra de paquete de viaje ----
def cancelarCompraTPV(vtas_id):
    """
    Cancela una compra de paquete de viaje, actualiza cupos y elimina registros relacionados.
    """
    venta = buscarVentaId(vtas_id)
    cantidad = venta[0]["Cantidad"]
    codigoViaje = venta[0]["Codigo de viaje"]

    cursor.execute(
        "UPDATE paquete_de_viajes SET cupos = cupos + %s WHERE codigo = %s",
        (cantidad, codigoViaje),
    )
    cursor.execute("DELETE FROM vtas_uc WHERE vtas_id = %s", (vtas_id,))
    cursor.execute("DELETE FROM ventas WHERE vtas_id = %s", (vtas_id,))

    cursor.commit()

    return {"Mensaje": "Compra cancelada"}
