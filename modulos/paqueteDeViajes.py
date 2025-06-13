# --- Coneccion BD ---
from main import cursor

# --- Convertir datos TVS a diccionario ---
import datetime


def convertirDatosTPV(respuesta):
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


# --- CRUD ---
# Create paquete de viaje
from controladores.date import convertirDate, convertirHora


def agregarPaquetedeViaje(data):
    hora = convertirHora(data.hora)
    fecha = convertirDate(data.fecha)

    cursor.execute(
        "INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
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
    cursor.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}


# Read paquete de viajes
def verPaquetedeViajes():
    cursor.execute("SELECT * FROM paquete_de_viajes")
    respuesta = cursor.fetchall()

    nrepuesta = convertirDatosTPV(respuesta)

    return nrepuesta


# Delete paquete de viaje
def quitarPaquetedeViaje(codigoDeViaje):
    cursor.execute("DELETE FROM paquete_de_viajes WHERE codigo = %s", (codigoDeViaje,))
    cursor.commit()

    return {"Mensaje": "Viaje borrado exitosamente"}
