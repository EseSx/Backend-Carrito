# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de viajes simples ---
from modulos.excursiones import agregarExcursiones

# -- Importar Base Models ---
from modulos.esquemas import Excursiones


# --- Rutas CRUD ---
# Create excursiones
@router.post("/ingresar")
def ingresar_excursiones(data: Excursiones):
    agregarExcursiones(data)
    return


# Read excursiones
@router.get("/obtener")
def retornar_viaje_simple():
    return verViajesSimples()


# Update viaje simple
@router.post("/modificar")
def modificar_viaje_simple():
    return


# Delete viaje simple
@router.post("/eliminar")
def eliminar_viaje_simple(codigoDeViaje):
    quitarViajesimple(codigoDeViaje)
    return
