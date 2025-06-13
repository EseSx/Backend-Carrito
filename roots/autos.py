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
)


# ===============================
#         Importación de Modelos
# ===============================

from modulos.esquemas import Auto, AutoID, VinculoVSaAuto, VinculoPVaAuto


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
    res = vinculaVSaAuto(data)
    return res


# ---- Crear nueva relacion de paquete de viaje a auto ----
@router.post("/ingresarVinculoPV")
async def ingresar_vinculos_PV(data: VinculoPVaAuto):
    res = vincularPVaAuto(data)
    return res


# ---- Obtener lista de autos ----
@router.get("/obtenerID")
async def retornar_autosPorID(data: AutoID):
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    res = verAutoID(data)
    return res


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
