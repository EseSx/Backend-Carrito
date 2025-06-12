# --- Coneccion BD ---
from main import cursor

# --- Convertir datos TVS a diccionario ---
import datetime


def convertirDatosTVS(respuesta):

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


# --- CRUD ---
from controladores.date import convertirDate, convertirHora


# Read viajes simples
def verViajesSimples():

    cursor.execute("SELECT * FROM viaje_simple")
    respuesta = cursor.fetchall()
    nrepuesta = convertirDatosTVS(respuesta)

    return nrepuesta


# Insert viajes simples
def agregarViajeSimple(
    codigo,
    nombre,
    descripcion,
    precio,
    origen,
    destino,
    transporte,
    fecha,
    hora,
    cupos,
    duracion_aprox,
    tipo_de_viaje,
    estado,
):
    cursor.execute(
        "INSERT INTO viaje_simple (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje, estado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            codigo,
            nombre,
            descripcion,
            precio,
            origen,
            destino,
            transporte,
            fecha,
            hora,
            cupos,
            duracion_aprox,
            tipo_de_viaje,
            estado,
        ),
    )
    hora = convertirHora(hora)
    fecha = convertirDate(fecha)
    cursor.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}


# Delete viajes simples
def quitarViajesimple(codigoDeViaje):
    cursor.execute("DELETE FROM viaje_simple WHERE codigo = %s", (codigoDeViaje,))
    cursor.commit()

    return {"Mensaje": "Viaje borrado exitosamente"}
