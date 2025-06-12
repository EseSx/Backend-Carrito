# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- rutas de viajes ---
from modulos.viajes import verViajesSimples


@router.get("/obtener")
def retornar_usuario():
    return {"Regreso": verViajesSimples()}
