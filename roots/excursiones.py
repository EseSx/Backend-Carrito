# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.excursiones import (
    agregarExcursiones,
    eliminarExcursion,
    paqueteViajesExcursion,
    buscarExcursionporId,
    verExcursionPaquete,
)

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import (
    Excursiones,
    ExcursionesID,
    VinculoPVaExc,
    Paquete_de_viajeID,
)


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


# ---- Crear nueva relacion paquete de viajes a excursion ----
@router.post("/ingresarVinculoPV")
def ingresar_vinculo_PV(data: VinculoPVaExc):
    """
    Recibe datos de una excursión y la agrega a la base de datos.
    """
    res = paqueteViajesExcursion(data)
    return res


# ---- Obtener todas las excursiones por ID ----
@router.post("/obtenerID")
def retornar_excursionesPorID(data: ExcursionesID):
    """
    Devuelve la lista de todas las excursiones almacenadas basandose en su ID.
    """
    res = buscarExcursionporId(data)
    return res


# ---- Obtener todas las excursiones relacionadas a un paquete de viajes ----
@router.post("/obtenerPV")
def retornar_excursionesPorPV(data: Paquete_de_viajeID):
    """
    Devuelve la lista de todas las excursiones almacenadas basandose en su ID.
    """
    res = verExcursionPaquete(data)
    return res


# ---- Modificar excursión existente ----
@router.post("/modificar")
def modificar_excursiones():
    """
    Actualiza los datos de una excursión existente.
    """
    return


# ---- Eliminar excursión por ID ----
@router.post("/eliminar")
def eliminar_excursiones(data: ExcursionesID):
    """
    Elimina una excursión dado su ID.
    """
    res = eliminarExcursion(data)
    return res
