# --- Importar conexión a la base de datos ---
from main import cursor, conexion

# --- Importar funciones relacionadas ---
from modulos.viajeSimple import quitarViajesimple
from modulos.paqueteDeViajes import quitarPaquetedeViaje

# ============================
#   Funciones para Viaje Simple
# ============================


def consultarCuposTVS(codigoViaje):
    """
    Verifica la cantidad de cupos disponibles para un viaje simple.
    Si no hay cupos, cambia el estado a 'No disponible'.
    """
    cursor.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
    resultado = cursor.fetchone()
    cupos = resultado[0]

    if cupos == 0:
        cursor.execute(
            "UPDATE viaje_simple SET estado = %s WHERE codigo = %s",
            ("No disponible", codigoViaje),
        )
        cursor.commit()
        return {"Mensaje": "Ya no tiene cupos disponibles."}
    else:
        cursor.execute(
            "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
            ("disponible", codigoViaje),
        )
        return {"Mensaje": "Sigue con cupos disponibles."}


def restarCupoTVS(codigoViaje, cantidad):
    """
    Descuenta cupos de un viaje simple si hay suficientes disponibles.
    """
    cursor.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
    ncupos = cursor.fetchall()

    if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
        cursor.execute(
            "UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        conexion.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {
            "Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"
        }


# =============================
#   Funciones para Paquete de Viajes
# =============================


def consultarCuposTPV(codigoViaje):
    """
    Verifica la cantidad de cupos disponibles para un paquete de viajes.
    Si no hay cupos, cambia el estado a 'No disponible'.
    """
    cursor.execute(
        "SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,)
    )
    resultado = cursor.fetchone()
    cupos = resultado[0]

    if cupos == 0:
        cursor.execute(
            "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
            ("No disponible", codigoViaje),
        )
        conexion.commit()
        return {"Mensaje": "Ya no tiene cupos disponibles."}
    else:
        cursor.execute(
            "UPDATE paquete_de_viajes SET estado = %s WHERE codigo = %s",
            ("disponible", codigoViaje),
        )
        return {"Mensaje": "Sigue con cupos disponibles."}


def restarCupoTPV(codigoViaje, cantidad):
    """
    Descuenta cupos de un paquete de viajes si hay suficientes disponibles.
    """
    cursor.execute(
        "SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,)
    )
    ncupos = cursor.fetchall()

    if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
        cursor.execute(
            "UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        conexion.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {
            "Mensaje": "No quedan cupos disponibles o no hay para esa cantidad, no se puede realizar la compra"
        }
