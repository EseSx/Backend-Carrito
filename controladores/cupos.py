# --- Importar conexión a la base de datos ---
from main import get_connection

# ============================
#   Funciones para Viaje Simple
# ============================


def consultarCuposTVS(codigoViaje):
    """
    Verifica la cantidad de cupos disponibles para un viaje simple.
    Si no hay cupos, cambia el estado a 'No disponible'.
    """
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
        resultado = cur.fetchone()
        cupos = resultado[0]

        if cupos == 0:
            cur.execute(
                "UPDATE viaje_simple SET estado = %s WHERE codigo = %s",
                ("No disponible", codigoViaje),
            )
            conn.commit()
            return {"Mensaje": "Ya no tiene cupos disponibles."}

        else:
            cur.execute(
                "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
                ("disponible", codigoViaje),
            )
            conn.commit()
            return {"Mensaje": "Sigue con cupos disponibles."}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def restarCupoTVS(codigoViaje, cantidad):
    """
    Descuenta cupos de un viaje simple si hay suficientes disponibles.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
        ncupos = cur.fetchall()

        if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
            cur.execute(
                "UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",
                (cantidad, codigoViaje),
            )
            conn.commit()

            return {"Mensaje": "Cupo decrementado exitosamente"}

        else:
            return {
                "Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"
            }

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# =============================
#   Funciones para Paquete de Viajes
# =============================


def consultarCuposTPV(codigoViaje):
    """
    Verifica la cantidad de cupos disponibles para un paquete de viajes.
    Si no hay cupos, cambia el estado a 'No disponible'.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,)
        )
        resultado = cur.fetchone()
        cupos = resultado[0]

        if cupos == 0:
            cur.execute(
                "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
                ("No disponible", codigoViaje),
            )
            conn.commit()
            return {"Mensaje": "Ya no tiene cupos disponibles."}

        else:
            cur.execute(
                "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
                ("disponible", codigoViaje),
            )
            return {"Mensaje": "Sigue con cupos disponibles."}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


def restarCupoTPV(codigoViaje, cantidad):
    """
    Descuenta cupos de un paquete de viajes si hay suficientes disponibles.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,)
        )
        ncupos = cur.fetchall()

        if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
            cur.execute(
                "UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",
                (cantidad, codigoViaje),
            )
            conn.commit()

            return {"Mensaje": "Cupo decrementado exitosamente"}

        else:
            return {
                "Mensaje": "No quedan cupos disponibles o no hay para esa cantidad, no se puede realizar la compra"
            }

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
