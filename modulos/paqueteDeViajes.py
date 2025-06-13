# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import get_connection
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
        hora = convertirHora(data.hora)
        fecha = convertirDate(data.fecha)

        cur.execute(
            "INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
                data.codigo,
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
                data.estado,
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
    """
    Elimina un paquete de viaje por su código.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM paquete_de_viajes WHERE codigo = %s", (codigoDeViaje,))
        conn.commit()

        return {"Mensaje": "Viaje borrado exitosamente"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
