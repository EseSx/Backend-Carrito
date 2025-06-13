# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de auto ---
from modulos.autos import agregarAuto, borrarAuto


# -- Importar Base Models ---
from modulos.esquemas import Auto


# --- Rutas CRUD ---
# Create auto
@router.post("/ingresar")
def ingresar_autos(data: Auto):
    agregarAuto(data)
    return


# Read auto
@router.get("/obtener")
def retornar_autos():
    return


# Update auto
@router.post("/modificar")
def modificar_autos():
    return


# Delete auto
@router.post("/eliminar")
def eliminar_autos(auto_id):
    borrarAuto(auto_id)
    return
