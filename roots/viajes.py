# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- rutas de viajes ---
from modulos.viajes import verViajesSimples


@router.get("/obtener")
def retornar_usuario():
    return {verViajesSimples()}


@router.get("/hola")
def retornar_hola():
    return {"msg": "hola"}
