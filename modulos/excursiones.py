# ===============================
#   Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#     funciones auxiliares
# ===============================

from controladores.date import convertirHora
from types import SimpleNamespace

# ===============================
#             CRUD
# ===============================


# ---- Insertar Excursión ----
def agregarExcursiones(data):
    """
    Inserta una nueva excursión en la base de datos.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT MAX(excursion_id) FROM excursiones")
        max_id = cur.fetchone()
        if max_id[0] is None:
            max_id = 1
        else:
            max_id = int(max_id[0]) + 1

        horaInicio = convertirHora(data.inicio)
        horaFinal = convertirHora(data.final)

        cur.execute(
            "INSERT INTO excursiones (excursion_id, nombre, inicio, final, descripcion, lugar) VALUES(%s,%s,%s,%s,%s,%s)",
            (
                max_id,
                data.nombre,
                horaInicio,
                horaFinal,
                data.descripcion,
                data.lugar,
            ),
        )
        conn.commit()

        return {"Mensaje": "Se ha agregado la excursion exitosamente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Eliminar Excursión ----
def eliminarExcursion(excursion_id):
    """
    Elimina las excurisones
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM pv_exc WHERE exc_id = %s", (excursion_id,))
        n = cur.fetchall()
        regExcPvIDs = []
        for i in n:

            regExcPvIDs.append(i[2])

        for id in regExcPvIDs:
            cur.execute("DELETE FROM pv_exc WHERE id = %s", (id,))
            conn.commit()

        cur.execute("DELETE FROM excursiones WHERE excursion_id = %s", (excursion_id,))
        conn.commit()

        return {"Mensaje": "Borrado exitosamente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Obtener excursion ----
def verExcursiones():
    """
    Obtiene todas las excurisones.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM excursiones")
        respuesta = cur.fetchall()
        excursiones = []

        for exc in respuesta:
            inicio = exc[2]
            inicio = inicio.strftime("%H:%M:%S")
            final = exc[3]
            final = final.strftime("%H:%M:%S")
            excursion = {
                "Excursion id": exc[0],
                "Nombre": exc[1],
                "Inicio": inicio,
                "Final": final,
                "Descripcion": exc[4],
                "Lugar": exc[5],
            }

            excursiones.append(excursion)
        return excursiones

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#  Relacionar Excursión & Paquete
# ===============================


def paqueteViajesExcursion(data):
    """
    Vincula una excursión con un paquete de viajes.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO pv_exc (pv_id, exc_id) VALUES (%s,%s)",
            (data.pv_id, data.exc_id),
        )
        conn.commit()

        return {"Mensaje": "Se ha vinculado una excursion con un paquete de viajes"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ===============================
#          Consultas
# ===============================


def buscarExcursionporId(data):
    """
    Busca una excursión por su ID y devuelve sus detalles.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM excursiones WHERE excursion_id = %s", (data.excursion_id,)
        )
        respuesta = cur.fetchall()
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

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def verExcursionPaquete(data):
    """
    Devuelve una lista de excursiones asociadas a un paquete de viaje.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT exc_id FROM pv_exc WHERE pv_id = %s", (data.pv_id,))
        respuesta = cur.fetchall()
        dicAutos = []
        for i in respuesta:
            data = SimpleNamespace(excursion_id=i[0])
            dicAutos.append(buscarExcursionporId(data))

        return dicAutos

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
