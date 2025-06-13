# --- Creacion del router ---
from fastapi import APIRouter

router = APIRouter()

# --- Importar CRUD de usuarios comunes ---

# -- Importar Base Models ---
from modulos.esquemas import Usuarios_comunes


# --- Rutas CRUD ---
# Create usuario
@router.post("/ingresar")
async def ingresar_usuario(data: Usuarios_comunes):
    # Funcion para ingresar clientes
    return


# Delete usuario
@router.post("/eliminar")
async def eliminar_usuario():
    # Funcion para eliminar clientes
    return
