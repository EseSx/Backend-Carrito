# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de excursiones ---
from modulos.excursiones import agregarExcursiones, eliminarExcursion

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
def retornar_excursiones():
    return


# Update excursiones
@router.post("/modificar")
def modificar_excursiones():
    return


# Delete excursiones
@router.post("/eliminar")
def eliminar_excursiones(excursion_id):
    eliminarExcursion(excursion_id)
    return
