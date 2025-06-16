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
    validarCliente,
    validarAdmin,
)

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import (
    Usuarios_comunes,
    Usuarios_comunes_id,
    Validacion_de_usuarios,
)


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nuevo usuario común ---- ANDA
@router.post("/ingresar")
async def ingresar_usuario(data: Usuarios_comunes):
    """
    Recibe los datos de un usuario común y lo crea en la base de datos.
    """
    res = crearCliente(data)
    return res


# ---- Obtener todos los usuarios comunes ----
@router.get("/obtener")
async def retornar_usuario():
    """
    Devuelve la lista de todos los usuarios comunes.
    """
    res = verClientes()
    return res


# ---- Eliminar usuario común por ID ----
@router.post("/eliminar")
async def eliminar_usuario(data: Usuarios_comunes_id):
    """
    Elimina un usuario común dado su ID.
    """
    res = eliminarUsuario(data)
    return res


# ---- Obtener usuario común por ID ----
@router.post("/obtenerId")
async def retornarPorID_usuario(data: Usuarios_comunes_id):
    """
    Devuelve los datos de un usuario común específico por ID.
    """
    res = verClienteId(data)
    return res


@router.post("/validarContraseña")
async def retornarValidacion(data: Validacion_de_usuarios):
    """
    Devuelve la validacion en formato booleano de si existe o no el usuario.
    """
    res = validarCliente(data)
    return res


@router.post("/validarContraseñaAdmin")
async def retornarValidacionAdmin(data: Validacion_de_usuarios):
    """
    Devuelve la validacion en formato booleano de si existe o no el administrador.
    """
    res = validarAdmin(data)
    return res
