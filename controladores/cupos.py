# --- Conexion con las BD ---
from main import cursor

# --- Manejar cupos TVS ---
from modulos.viajeSimple import quitarViajesimple


def consultarCuposTVS(codigoViaje):
    cursor.execute("SELECT cupo FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
    ncupos = cursor.fetchall()

    if ncupos == 0:
        quitarViajesimple(codigoViaje)
    else:
        return {"Mensaje": "Sigue con cupos disponibles."}


def restarCupoTVS(codigoViaje, cantidad):
    cursor.execute("SELECT cupos FROM viaje_simple WHERE codigo = %s", (codigoViaje,))
    ncupos = cursor.fetchall()

    if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
        cursor.execute(
            "UPDATE viaje_simple SET cupos = cupos - %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        cursor.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {
            "Mensaje": "No quedan cupos disponibles, no se puede realizar la compra"
        }


# --- Manejar cupos TPV ---
from modulos.paqueteDeViajes import quitarPaquetedeViaje


def consultarCuposTPV(codigoViaje):
    cursor.execute(
        "SELECT cupo FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje)
    )
    ncupos = cursor.fetchall()

    if ncupos == 0:
        quitarPaquetedeViaje(codigoViaje)
    else:
        return {"Mensaje": "Sigue con cupos disponibles."}


def restarCupoTPV(codigoViaje, cantidad):

    cursor.execute(
        "SELECT cupos FROM paquete_de_viajes WHERE codigo = %s", (codigoViaje,)
    )
    ncupos = cursor.fetchall()

    if cantidad < ncupos[0][0] or cantidad == ncupos[0][0]:
        cursor.execute(
            "UPDATE paquete_de_viajes SET cupos = cupos - %s WHERE codigo = %s",
            (cantidad, codigoViaje),
        )
        cursor.commit()

        return {"Mensaje": "Cupo decrementado exitosamente"}

    else:
        return {
            "Mensaje": "No quedan cupos disponibles o no hay para esa cantidad, no se puede realizar la compra"
        }
