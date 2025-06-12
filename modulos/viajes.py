# --- Coneccion con la BD ---
import psycopg2
import datetime  # Para convertir variables a tipo date para postgre

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns)
cursor = conexionViajes.cursor()


# --- Normalizacion de datos ---
# Datos de viajes simples
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
            }
        )
        # dicConvertido.append()
        registroListas.append(dicConvertido)

    return registroListas


# Datos de paquetes de viajes
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
            }
        )

        registroListas.append(dicConvertido)
    return registroListas


# --- CRUD Viajes ---
# Viaje simple
def verViajesSimples():
    cursor.execute("SELECT * FROM viaje_simple")
    respuesta = cursor.fetchall()

    nrepuesta = convertirDatosTVS(respuesta)

    return nrepuesta


# Paquetes de viaje
def verPaquetedeViajes():
    cursor.execute("SELECT * FROM paquete_de_viajes")
    respuesta = cursor.fetchall()

    nrepuesta = convertirDatosTPV(respuesta)

    return nrepuesta


# Funcion especifica ver excursiones dw un viaje en especifico
def verExcursiones(codigoViaje):
    cursor.execute("SELECT * FROM excursiones WHERE ID")


def restarCupoTVS(codigoViaje, cantidad):
    cursor.execute("SELECT cupo FROM viaje_simple WHERE codigo = %s", (codigoViaje))
    ncupos = cursor.fetchall()

    if codigoViaje > ncupos or codigoViaje == ncupos:
        cursor.execute(
            "UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        conexionViajes.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {
            "Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"
        }


# Para tabla de paquetes de viajes
def restarCupoTPV(codigoViaje, cantidad):
    cursor.execute(
        "UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",
        (cantidad, codigoViaje),
    )
    conexionViajes.commit()

    return {"Mensaje": "Cupo decrementado"}


# Metodo que solo aplicaria para el frontened del admin
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
):
    cursor.execute(
        "INSERT INTO viaje_simple (codigo, nombre, descripcion, precio, origen, destino, transporte, fecha, hora, cupos, duracion_aprox, tipo_de_viaje) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
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
        ),
    )
    conexionViajes.commit()

    return {"Mensaje": "Nuevo viaje simple agregado"}


# Metodo que solo aplicaria para el frontened del admin
def agregarPaquetedeViaje(
    codigo,
    nombre,
    precio,
    origen,
    destino,
    estadia,
    tipo,
    descripcion,
    cupos,
    duracion,
    tipo_de_viaje,
    hora,
    fecha,
):
    cursor.execute(
        "INSERT INTO paquete_de_viajes (codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            codigo,
            nombre,
            precio,
            origen,
            destino,
            estadia,
            tipo,
            descripcion,
            cupos,
            duracion,
            tipo_de_viaje,
            hora,
            fecha,
        ),
    )
    conexionViajes.commit()
    # --------- Revisar porque esta incopleta hay que ver que metodos usar para ingresar excursiones --------

    return {"Mensaje": "Nuevo viaje simple agregado"}


def quitarViajesimple(codigoDeViaje):
    cursor.execute("DELETE * FROM viaje_simple WHERE codigo = %s", (codigoDeViaje))
    conexionViajes.commit()

    return {"Mensaje": "Viaje borrado exitosamente"}


def quitarPaquetedeViaje(codigoDeViaje):
    cursor.execute("DELETE * FROM paquete_de_viaje WHERE codigo = %s", (codigoDeViaje))
    conexionViajes.commit()

    return {"Mensaje": "Viaje borrado exitosamente"}


# Hacer una funcion que verifique constantemente que los viajes no tenga 0 cupos porque si es 0 eliminamos el registro de la bd, siempre se ejuctaria i guess
def consultarCuposTVS(codigoViaje):
    cursor.execute("SELECT cupo FROM viaje_simple WHERE codigo = %s", (codigoViaje))
    ncupos = cursor.fetchall()

    if ncupos == 0:
        quitarViajesimple(codigoViaje)
    else:
        return {"Mensaje": "Sigue con cupos disponibles."}


# Lo mismo para la tabla paquetes_de_viajes
def consultarCuposTPV(codigoViaje):
    cursor.execute(
        "SELECT cupo FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje)
    )
    ncupos = cursor.fetchall()

    if ncupos == 0:
        quitarPaquetedeViaje(codigoViaje)
    else:
        return {"Mensaje": "Sigue con cupos disponibles."}


# Funcion Para hacer tipo dae
def convertirDate(fecha):
    # 24/10/2006
    nfecha = datetime.strptime(fecha, "%d/%m/%y").date()
    return nfecha


def convertirHora(hora):
    # La hora debe estar pasada de esta manera "10:00" como un string.
    nhora = datetime.strptime(hora, "%H:%M").time()
    return nhora


"""agregarViajeSimple(672822248,"Cordoba", "Viaje rapido a Cordoba", 30000, "Puerto Madero", "Cordoba", "Autobus", convertirDate("2/11/25"), convertirHora("9:00") , 50, "1 dia" , "Ida")
agregarPaquetedeViaje(7515, "Vacaciones a Italia", 90000, "Buenos Aires, Aeropuerto", "Italia" ,"10 dias en Italia, hotel Libertador servicio todo incluido", "Ida y Vuelta", "Viaje ideal para viaje solitario, para conocer nuevos paises", 70, "2 dias","Internacional",convertirHora("22:00"), convertirDate("10/11/25"))

agregarViajeSimple(676713848,"Jamaica", "Vuelo a Jamaica", 30000, "Buenos Aires, Aeropuerto", "Jamaica", "Avion", convertirDate("2/11/25"), convertirHora("9:00") , 50, "2 dias" , "Ida y Vuelta")
agregarPaquetedeViaje(715, "Vacaciones a Brasil", 10000, "Buenos Aires, Aeropuerto", "Brasil" ,"7 dias en Brasil, hotel Libertador servicio todo incluido", "Ida y Vuelta", "Viaje ideal para toda la familia en dias festivos, para conocer nuevos paises. Una experiencia unica.", 70, "1 dia","Internacional",convertirHora("22:00"), convertirDate("10/11/25"))

agregarViajeSimple(6777848,"Marruecos", "Viaje rapido a Marruecos", 20000, "Buenos Aires, Aeropuerto", "Marruecos", "Avion", convertirDate("2/11/25"), convertirHora("9:00") , 50, "2 dias" , "Ida")
agregarPaquetedeViaje(7500, "Vacaciones a Haiti", 90000, "Buenos Aires, Aeropuerto", "Haiti" ,"10 dias en Haiti, hotel Libertador servicio todo incluido", "Ida y Vuelta", "Viaje ideal para viaje solitario, para conocer nuevos paises", 70, "2 dias","Internacional",convertirHora("22:00"), convertirDate("10/11/25"))
#codigo, nombre, precio, origen, destino, estadia, tipo, descripcion, cupos, duracion, tipo_de_viaje, hora, fecha"""

"""print(convertirHora("10:00"))
print(convertirDate("24/10/06"))"""


# quitarPaquetedeViaje(2455)

"""r = verViajesSimples()
print(r[2])
#print(verPaquetedeViajes())"""
r = verPaquetedeViajes()
print(r)


"""cursor.execute("SELECT fecha, hora FROM paquete_de_viajes")
respuesta = cursor.fetchall()"""

# print(respuesta[0][0])
"""cursor.execute("SELECT * FROM paquete_de_viajes")
respuesta = cursor.fetchall()
registrosLista = []
for registro in respuesta:
    #print("------------ registro 1 -----")
    diccionario = {"codigo": registro[0], "Nombre": registro[1]}
    for item in registro:
        print(item)
        print("$$$$$")
print(diccionario)"""


# print(respuesta(1))


# print(convertirHora("22:00"), convertirDate("10/11/25"))
