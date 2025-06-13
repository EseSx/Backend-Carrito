# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de paquetes de viaje ---
from modulos.paqueteDeViajes import (
    agregarPaquetedeViaje,
    verPaquetedeViajes,
    quitarPaquetedeViaje,
)

# -- Importar Base Models ---
from modulos.esquemas import Paquete_de_viaje


# --- Rutas CRUD ---
# Create paquetes de viaje
@router.post("/ingresar")
def ingresar_paquetesDeViaje(data: Paquete_de_viaje):
    agregarPaquetedeViaje(data)
    return


# Read paquetes de viaje
@router.get("/obtener")
def retornar_paquetesDeViaje():
    verPaquetedeViajes()
    return


# Update paquetes de viaje
@router.post("/modificar")
def modificar_paquetesDeViaje():
    return


# Delete paquetes de viaje
@router.post("/eliminar")
def eliminar_paquetesDeViaje(codigoDeViaje):
    quitarPaquetedeViaje(codigoDeViaje)
    return
