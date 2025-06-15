# ==============================
#   Conversión de fecha y hora
# ==============================
import datetime
from datetime import datetime


def convertirDate(fecha):
    """
    Convierte una cadena de fecha en formato 'dd/mm/yy' a un objeto datetime.date.
    """
    nfecha = datetime.strptime(fecha, "%d/%m/%y").date()
    return nfecha


def convertirHora(hora):
    """
    Convierte una cadena de hora en formato 'HH:MM' a un objeto datetime.time.
    """
    nhora = datetime.strptime(hora, "%H:%M").time()
    return nhora


def conseguirDatoActual():
    """
    Devuelve la fecha y hora actual
    """
    ahora = datetime.now()

    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M")

    return {"fecha": fecha, "hora": hora}
