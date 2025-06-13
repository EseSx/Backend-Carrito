# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de ventas ---
from modulos.ventas import sumarVenta, verVentas

# -- Importar Base Models ---
from modulos.esquemas import Ventas


# --- Rutas CRUD ---
# Create ventas
@router.post("/ingresar")
def ingresar_ventas(data: Ventas):
    sumarVenta(data)
    return


# Read ventas
@router.get("/obtener")
def retornar_ventas():
    verVentas()
    return


# Update ventas
@router.post("/modificar")
def modificar_ventas():
    return


# Delete ventas
@router.post("/eliminar")
def eliminar_ventas():
    return
