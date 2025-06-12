# --- Convertir a formato DATE ---
import datetime


def convertirDate(fecha):
    nfecha = datetime.strptime(fecha, "%d/%m/%y").date()
    return nfecha


def convertirHora(hora):
    nhora = datetime.strptime(hora, "%H:%M").time()
    return nhora
