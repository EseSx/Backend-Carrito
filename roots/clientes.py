# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.usuarioComun import (
    crearCliente,
    verClientes,
    verClienteId,
    eliminarUsuario,
)

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Usuarios_comunes


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nuevo usuario común ----
@router.post("/ingresar")
async def ingresar_usuario(data: Usuarios_comunes):
    """
    Recibe los datos de un usuario común y lo crea en la base de datos.
    """
    crearCliente(data)
    return


# ---- Obtener todos los usuarios comunes ----
@router.get("/obtener")
async def retornar_usuario():
    """
    Devuelve la lista de todos los usuarios comunes.
    """
    verClientes()
    return


# ---- Eliminar usuario común por ID ----
@router.post("/eliminar")
async def eliminar_usuario(uc_id):
    """
    Elimina un usuario común dado su ID.
    """
    eliminarUsuario(uc_id)
    return


# ---- Obtener usuario común por ID ----
@router.post("/obtenerId")
async def retornarPorID_usuario(uc_id):
    """
    Devuelve los datos de un usuario común específico por ID.
    """
    verClienteId(uc_id)
    return
