# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#       Funciones auxiliares
# ===============================

import datetime
from controladores.date import convertirDate, convertirHora


def convertirDatosTVS(respuesta):
    """
    Convierte la lista de tuplas resultado de la consulta en una lista
    de diccionarios con formato adecuado para fechas y horas.
    """
    registroListas = []
    for item in respuesta:
        dicConvertido = []
        fecha = item[7]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = item[8]
        hora = hora.strftime("%H:%M:%S")

        dicConvertido = {
            "Codigo": item[0],
            "Nombre": item[1],
            "Descripcion": item[2],
            "Precio": item[3],
            "Origen": item[4],
            "Destino": item[5],
            "Transporte": item[6],
            "Fecha": fecha,
            "Hora": hora,
            "Cupos": item[9],
            "Duracion": item[10],
            "Tipo_de_viaje": item[11],
            "Estado": item[12],
        }
        registroListas.append(dicConvertido)
    return registroListas


# ===============================
#             CRUD
# ===============================


# ---- Leer todos los viajes simples ----
def verViajesSimples():
    """
    Recupera todos los viajes simples de la base de datos y los devuelve
    en formato de lista de diccionarios con fechas y horas formateadas.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM viaje_simple")
        respuesta = cur.fetchall()
        nrepuesta = convertirDatosTVS(respuesta)

        return nrepuesta

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Agregar un nuevo viaje simple ----
def agregarViajeSimple(data):
    """
    Inserta un nuevo viaje simple en la base de datos,
    convirtiendo la fecha y la hora al formato adecuado.
    """
    hora = convertirHora(data.hora)
    fecha = convertirDate(data.fecha)

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT MAX(codigo) FROM viaje_simple")
        max_id = cur.fetchone()
        if max_id[0] is None:
            max_id = 1
        else:
            max_id = int(max_id[0]) + 1
        cur.execute(
            "INSERT INTO viaje_simple (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                max_id,
                data.nombre,
                data.descripcion,
                data.precio,
                data.origen,
                data.destino,
                data.transporte,
                fecha,
                hora,
                data.cupos,
                data.duracion_aprox,
                data.tipo_de_viaje,
                "Disponible",
            ),
        )
        conn.commit()

        return {"Mensaje": "Nuevo viaje simple agregado"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Eliminar un viaje simple por código ----
def quitarViajesimple(codigoDeViaje):
    """
    Elimina viajes por el codigo de viaje
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT id FROM vs_at WHERE vs_id = %s", (codigoDeViaje,))
        r = cur.fetchall()
        regVsAtIdDs = []
        for i in r:
            regVsAtIdDs.append(i[0])

        for registroId in regVsAtIdDs:
            cur.execute("DELETE FROM vs_at WHERE id = %s", (registroId,))
            conn.commit()

        cur.execute("DELETE FROM viaje_simple WHERE codigo = %s", (codigoDeViaje,))
        conn.commit()

        return {"Mensaje": "Viaje borrado exitosamente"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
