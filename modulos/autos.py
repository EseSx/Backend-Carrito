# ===============================
#   Conexión con la Base de Datos
# ===============================

from main import get_connection, cursor, conexion


# ===============================
#           CRUD Autos
# ===============================


def agregarAuto(data):
    """
    Inserta un nuevo auto en la tabla 'autos'.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO auto (auto_id, modelo, disponibles, precio_por_dia) VALUES(%s,%s,%s,%s)",
            (data.auto_id, data.modelo, data.disponibles, data.precio_por_dia),
        )
        conn.commit()

        return {"mensaje": "Nuevo auto cargado exitosamente"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()


def borrarAuto(auto_id):
    """
    Elimina un auto de la tabla 'autos' por su ID.
    """
    cursor.execute("DELETE FROM autos WHERE auto_id = %s", (auto_id,))

    return {"Mensaje": "Auto eliminado exitosamente"}


# ===============================
#   Vincular autos a viajes
# ===============================


def vinculaVSaAuto(vs_id, at_id):
    """
    Vincula un auto (at_id) a un viaje simple (vs_id).
    """

    cursor.execute("INSERT INTO vs_at (vs_id, at_id) VALUES(%s,%s)", (vs_id, at_id))
    conexion.commit()

    return {"Mensaje": "Se ha asignado un auto a un viaje simple"}


def vincularPVaAuto(pv_id, at_id):
    """
    Vincula un auto (at_id) a un paquete de viajes (pv_id).
    """
    cursor.execute("INSERT INTO exc_at (pv_id, at_id) VALUES(%s,%s)", (pv_id, at_id))

    return {"Mensaje": "Se ha asignado un auto a un paquete de viajes"}


# ===============================
#         Consultar autos
# ===============================


def verAutoID(auto_id):
    """
    Devuelve la información de un auto por su ID.
    """
    cursor.execute("SELECT * FROM auto WHERE auto_Id = %s", (auto_id,))
    respuesta = cursor.fetchall()
    respuesta = {
        "auto id": respuesta[0][0],
        "modelo": respuesta[0][1],
        "disponibles": respuesta[0][2],
        "precio por dia": respuesta[0][3],
    }

    return respuesta


def verAutoPV(pv_id):
    """
    Devuelve todos los autos vinculados a un paquete de viajes.
    """
    cursor.execute("SELECT * FROM exc_at WHERE pv_id = %s", (pv_id,))
    respuesta = cursor.fetchall()
    autos = []
    autoInfo = []
    for i in respuesta[0]:
        autos.append(respuesta[1][1])
    for auto in autos:
        r = verAutoID(auto)
        autoInfo.append(r)

    return autoInfo


def verAutoVs(vs_id):
    """
    Devuelve todos los autos vinculados a un viaje simple.
    """
    cursor.execute("SELECT * FROM vs_at WHERE vs_id = %s", (vs_id,))
    respuesta = cursor.fetchall()
    autos = []
    autoInfo = []
    for i in respuesta[0]:
        autos.append(respuesta[1][1])
    for auto in autos:
        r = verAutoID(auto)
        autoInfo.append(r)

    return autoInfo
