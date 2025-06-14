# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#         Importación de CRUD
# ===============================

from modulos.autos import (
    agregarAuto,
    borrarAuto,
    vinculaVSaAuto,
    vincularPVaAuto,
    verAutoID,
    verAutoPV,
    verAutoVs,
)


# ===============================
#         Importación de Modelos
# ===============================

from modulos.esquemas import (
    Auto,
    AutoID,
    VinculoVSaAuto,
    VinculoPVaAuto,
    Paquete_de_viajeID,
    Viaje_simpleID,
)


# ===============================
#             Rutas CRUD
# ===============================


# ---- Crear nuevo auto ----
@router.post("/ingresar")
async def ingresar_autos(data: Auto):
    """
    Recibe los datos de un auto y llama a la función para agregarlo a la base.
    """
    res = agregarAuto(data)
    return res


# ---- Crear nueva relacion de viaje simple a auto ----
@router.post("/ingresarVinculoVS")
async def ingresar_vinculos_VS(data: VinculoVSaAuto):
    """
    Recibe los ids de un auto y un viaje simple, llama a la funcion para agregar la relacion
    """
    res = vinculaVSaAuto(data)
    return res


# ---- Crear nueva relacion de paquete de viaje a auto ----
@router.post("/ingresarVinculoPV")
async def ingresar_vinculos_PV(data: VinculoPVaAuto):
    """
    Recibe los ids de un auto y un paquete de viaje, llama a la funcion para agregar la relacion
    """
    res = vincularPVaAuto(data)
    return res


# ---- Obtener lista de autos por ID ----
@router.post("/obtenerID")
async def retornar_autosPorID(data: AutoID):
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    res = verAutoID(data)
    return res


# ---- Obtener lista de autos relacionados a un paquete de viajes ----
@router.post("/obtenerPV")
async def retornar_autosPorPV(data: Paquete_de_viajeID):
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    res = verAutoPV(data)
    return res


# ---- Obtener lista de autos relacionados a un viaje simple ----
@router.post("/obtenerVS")
async def retornar_autosPorVS(data: Viaje_simpleID):
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    res = verAutoVs(data)
    return res


# Preguntar si no vamos a añadir
# ---- Modificar datos de un auto ----
@router.post("/modificar")
async def modificar_autos():
    """
    Actualiza los datos de un auto existente (pendiente implementación).
    """
    return


# ---- Eliminar un auto por ID ----
@router.post("/eliminar")
async def eliminar_autos(data: AutoID):
    """
    Elimina un auto de la base de datos utilizando su ID.
    """
    res = borrarAuto(data)
    return res
