# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.excursiones import agregarExcursiones, eliminarExcursion

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Excursiones


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nueva excursión ----
@router.post("/ingresar")
def ingresar_excursiones(data: Excursiones):
    """
    Recibe datos de una excursión y la agrega a la base de datos.
    """
    res = agregarExcursiones(data)
    return res


# ---- Obtener todas las excursiones ----
@router.get("/obtener")
def retornar_excursiones():
    """
    Devuelve la lista de todas las excursiones almacenadas.
    """
    return


# ---- Modificar excursión existente ----
@router.post("/modificar")
def modificar_excursiones():
    """
    Actualiza los datos de una excursión existente.
    """
    return


# ---- Eliminar excursión por ID ----
@router.post("/eliminar")
def eliminar_excursiones(excursion_id):
    """
    Elimina una excursión dado su ID.
    """
    res = eliminarExcursion(excursion_id)
    return res
