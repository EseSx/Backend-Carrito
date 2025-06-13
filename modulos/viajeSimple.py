# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import cursor
import datetime

# ===============================
#       Funciones auxiliares
# ===============================


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

        dicConvertido.append(
            {
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
        )
        registroListas.append(dicConvertido)
    return registroListas


# ===============================
#             CRUD
# ===============================

from controladores.date import convertirDate, convertirHora


# ---- Leer todos los viajes simples ----
def verViajesSimples():
    """
    Recupera todos los viajes simples de la base de datos y los devuelve
    en formato de lista de diccionarios con fechas y horas formateadas.
    """
    cursor.execute("SELECT * FROM viaje_simple")
    respuesta = cursor.fetchall()
    nrepuesta = convertirDatosTVS(respuesta)

    return nrepuesta


# ---- Agregar un nuevo viaje simple ----
def agregarViajeSimple(data):
    """
    Inserta un nuevo viaje simple en la base de datos,
    convirtiendo la fecha y la hora al formato adecuado.
    """
    hora = convertirHora(data.hora)
    fecha = convertirDate(data.fecha)

    cursor.execute(
        "INSERT INTO viaje_simple (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            data.codigo,
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
            data.estado,
        ),
    )
    cursor.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}


# ---- Eliminar un viaje simple por código ----
def quitarViajesimple(codigoDeViaje):
    """
    Elimina un viaje simple de la base de datos según su código.
    """
    cursor.execute("DELETE FROM viaje_simple WHERE codigo = %s", (codigoDeViaje,))
    cursor.commit()

    return {"Mensaje": "Viaje borrado exitosamente"}
