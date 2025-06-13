# ===============================
#   Conexión con la Base de Datos
# ===============================

from main import cursor


# ===============================
#             CRUD
# ===============================


# ---- Insertar Excursión ----
def agregarExcursiones(data):
    """
    Inserta una nueva excursión en la base de datos.
    """
    cursor.execute(
        "INSERT INTO excursiones (nombre, inicio, final, descripcion, lugar) VALUES(%s,%s,%s,%s,%s)",
        (data.nombre, data.inicio, data.final, data.descripcion, data.lugar),
    )
    cursor.commit()

    return {"Mensaje": "Se ha agregado la excursion exitosamente"}


# ---- Eliminar Excursión ----
def eliminarExcursion(excursion_id):
    """
    Elimina una excursión por su ID.
    """
    cursor.execute("DELETE FROM excursiones WHERE excursion_id = %s", (excursion_id,))
    cursor.commit()

    return {"Mensaje": "Borrado exitosamente"}


# ===============================
#  Relacionar Excursión & Paquete
# ===============================


def paqueteViajesExcursion(pv_id, exc_id):
    """
    Vincula una excursión con un paquete de viajes.
    """
    cursor.execute("INSERT INTO pv_exc (pv_id, exc_id) VALUES (%s,%s)", (pv_id, exc_id))
    cursor.commit()

    return {"Mensaje": "Se ha vinculado una excursion con un paquete de viajes"}


# ===============================
#          Consultas
# ===============================


def buscarExcursionporId(excursion_id):
    """
    Busca una excursión por su ID y devuelve sus detalles.
    """
    cursor.execute("SELECT * FROM excursiones WHERE excursion_id = %s", (excursion_id,))
    respuesta = cursor.fetchall()
    dicExcursiones = []

    inicio = respuesta[0][2]
    inicio = inicio.strftime("%H:%M:%S")
    final = respuesta[0][3]
    final = final.strftime("%H:%M:%S")

    dicExcursiones.append(
        {
            "Excursion id": respuesta[0][0],
            "Nombre": respuesta[0][1],
            "Inicio": inicio,
            "Final": final,
            "Descripcion": respuesta[0][4],
            "Lugar": respuesta[0][5],
        }
    )

    return dicExcursiones


def verExcursionPaquete(pv_id):
    """
    Devuelve una lista de excursiones asociadas a un paquete de viaje.
    """
    cursor.execute("SELECT exc_id FROM pv_exc WHERE pv_id = %s", (pv_id,))
    respuesta = cursor.fetchall()
    lista_pv_ids = []
    for excursion in respuesta:
        lista_pv_ids.append(excursion[0])

    excursiones = []
    for i in lista_pv_ids:
        r = buscarExcursionporId(i)
        excursiones.append(r)

    return excursiones
