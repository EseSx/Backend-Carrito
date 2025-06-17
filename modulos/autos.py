# ===============================
#   Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#     funciones auxiliares
# ===============================

from types import SimpleNamespace

# ===============================
#           CRUD Autos
# ===============================


def agregarAuto(data):
    """
    Inserta un nuevo auto en la tabla 'auto'.
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT MAX(auto_id) FROM auto")
        max_id = cur.fetchone()
        if max_id[0] is None:
            max_id = 1
        else:
            max_id = int(max_id[0]) + 1

        cur.execute(
            "INSERT INTO auto (auto_id, modelo, disponibles, precio_por_dia) VALUES(%s,%s,%s,%s)",
            (max_id, data.modelo, data.disponibles, data.precio_por_dia),
        )
        conn.commit()

        return {"mensaje": "Nuevo auto cargado exitosamente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def borrarAuto(data):
    """
    Elimina un auto de la tabla 'auto' por su ID.
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM auto WHERE auto_id = %s", (data.auto_id,))
        conn.commit()

        return {"Mensaje": "Auto eliminado exitosamente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def verAutos():
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT *  FROM auto")
        respuesta = cur.fetchall()
        autos = []
        for auto in respuesta:
            at = {
                "auto id": auto[0],
                "modelo": auto[1],
                "disponibles": auto[2],
                "precio por dia": auto[3],
            }

            autos.append(at)

        return autos
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#   Vincular autos a viajes
# ===============================


def vinculaVSaAuto(data):
    """
    Vincula un auto (at_id) a un viaje simple (vs_id).
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO vs_at (vs_id, at_id) VALUES(%s,%s)", (data.vs_id, data.at_id)
        )
        conn.commit()

        return {"Mensaje": "Se ha asignado un auto a un viaje simple"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def vincularPVaAuto(data):
    """
    Vincula un auto (at_id) a un paquete de viajes (pv_id).
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO exc_at (pv_id, at_id) VALUES(%s,%s)", (data.pv_id, data.at_id)
        )
        conn.commit()

        return {"Mensaje": "Se ha asignado un auto a un paquete de viajes"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#         Consultar autos
# ===============================


def verAutoID(data):
    """
    Devuelve la información de un auto por su ID.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM auto WHERE auto_Id = %s", (data.auto_id,))
        respuesta = cur.fetchall()
        respuesta = {
            "auto id": respuesta[0][0],
            "modelo": respuesta[0][1],
            "disponibles": respuesta[0][2],
            "precio por dia": respuesta[0][3],
        }

        return respuesta

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def verAutoPV(data):
    """
    Devuelve todos los autos vinculados a un paquete de viajes.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT at_id FROM exc_at WHERE pv_id = %s", (data.pv_id,))
        respuesta = cur.fetchall()

        dicAutos = []
        for i in respuesta:
            data = SimpleNamespace(auto_id=i[0])
            dicAutos.append(verAutoID(data))

        return dicAutos

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def verAutoVs(data):
    """
    Devuelve todos los autos vinculados a un viaje simple.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT at_id FROM vs_at WHERE vs_id = %s", (data.vs_id,))
        respuesta = cur.fetchall()
        dicAutos = []
        for i in respuesta:
            data = SimpleNamespace(auto_id=i[0])
            dicAutos.append(verAutoID(data))

        return dicAutos

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
