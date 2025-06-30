# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#     funciones auxiliares
# ===============================

import datetime
from controladores.date import convertirDate, convertirHora

# ===============================
#             CRUD
# ===============================


# ---- Convertir datos paquete de viaje a diccionario ----
def convertirDatosTPV(respuesta):
    """
    Convierte la respuesta de la BD a lista de diccionarios con formato de fecha y hora.
    """
    registroListas = []
    for item in respuesta:
        dicConvertido = []
        fecha = item[12]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = item[11]
        hora = hora.strftime("%H:%M:%S")
        dicConvertido.append(
            {
                "Codigo": item[0],
                "Nombre": item[1],
                "Precio": item[2],
                "Origen": item[3],
                "Destino": item[4],
                "Estadia": item[5],
                "Tipo": item[6],
                "Descripcion": item[7],
                "Cupos": item[8],
                "Duracion": item[9],
                "Tipo_de_viaje": item[10],
                "Hora": hora,
                "Fecha": fecha,
                "Estado": item[13],
            }
        )
        registroListas.append(dicConvertido)
    return registroListas


# ---- Insertar paquete de viaje ----
def agregarPaquetedeViaje(data):
    """
    Inserta un nuevo paquete de viaje en la base de datos.
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT MAX(codigo) FROM paquete_de_viajes")
        max_id = cur.fetchone()
        if max_id[0] is None:
            max_id = 1
        else:
            max_id = int(max_id[0]) + 1
        hora = convertirHora(data.hora)
        fecha = convertirDate(data.fecha)

        cur.execute(
            "INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                max_id,
                data.nombre,
                data.precio,
                data.origen,
                data.destino,
                data.estadia,
                data.tipo,
                data.descripcion,
                data.cupos,
                data.duracion,
                data.tipo_de_viaje,
                hora,
                fecha,
                "Disponible",
            ),
        )
        conn.commit()

        return {"Mensaje": "Nuevo paquetede viajes agregado"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Consultar todos los paquetes de viaje ----
def verPaquetedeViajes():
    """
    Devuelve una lista con todos los paquetes de viaje.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM paquete_de_viajes")
        respuesta = cur.fetchall()

        nrepuesta = convertirDatosTPV(respuesta)

        return nrepuesta

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Eliminar paquete de viaje ----
def quitarPaquetedeViaje(codigoDeViaje):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM pv_exc WHERE pv_id = %s", (codigoDeViaje,))
        n = cur.fetchall()
        regPvExcIDs = []
        for i in n:

            regPvExcIDs.append(i[2])

        for id in regPvExcIDs:
            cur.execute("DELETE FROM pv_exc WHERE id = %s", (id,))
            conn.commit()

        cur.execute("SELECT id FROM exc_at WHERE pv_id = %s", (codigoDeViaje,))
        r = cur.fetchall()
        regPvAtIdDs = []
        for i in r:
            regPvAtIdDs.append(i[0])

        for registroId in regPvAtIdDs:
            cur.execute("DELETE FROM exc_at WHERE id = %s", (registroId,))
            conn.commit()

        cur.execute("DELETE FROM paquete_de_viajes WHERE codigo = %s", (codigoDeViaje,))
        conn.commit()

        return {"Mensaje": "Viaje borrado exitosamente"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
