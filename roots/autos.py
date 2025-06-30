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
    verAutos,
)


# ===============================
#         Importación de Modelos
# ===============================

from modulos.esquemas import (
    Auto,
    Auto_id,
    Vinculo_vs_a_auto,
    Vinculo_pv_a_auto,
    Paquete_de_viaje_id,
    Viaje_simple_id,
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
async def ingresar_vinculos_VS(data: Vinculo_vs_a_auto):
    """
    Recibe los ids de un auto y un viaje simple, llama a la funcion para agregar la relacion
    """
    res = vinculaVSaAuto(data)
    return res


# ---- Crear nueva relacion de paquete de viaje a auto ----
@router.post("/ingresarVinculoPV")
async def ingresar_vinculos_PV(data: Vinculo_pv_a_auto):
    """
    Recibe los ids de un auto y un paquete de viaje, llama a la funcion para agregar la relacion
    """
    res = vincularPVaAuto(data)
    return res


# ---- Obtener lista de autos ----
@router.get("/obtener")
async def retornar_autos():
    """
    Devuelve la lista de autos almacenados.
    """
    res = verAutos()
    return res


# ---- Obtener lista de autos por ID ----
@router.post("/obtenerID")
async def retornar_autosPorID(data: Auto_id):
    """
    Devuelve la lista de autos almacenados por id.
    """
    res = verAutoID(data)
    return res


# ---- Obtener lista de autos relacionados a un paquete de viajes ----
@router.post("/obtenerPV")
async def retornar_autosPorPV(data: Paquete_de_viaje_id):
    """
    Devuelve la lista de autos almacenados por paquete de viaje.
    """
    res = verAutoPV(data)
    return res


# ---- Obtener lista de autos relacionados a un viaje simple ----
@router.post("/obtenerVS")
async def retornar_autosPorVS(data: Viaje_simple_id):
    """
    Devuelve la lista de autos almacenados por viaje simple.
    """
    res = verAutoVs(data)
    return res


# ---- Eliminar un auto por ID ----
@router.post("/eliminar")
async def eliminar_autos(data: Auto_id):
    """
    Elimina un auto de la base de datos utilizando su ID.
    """
    res = borrarAuto(data.auto_id)
    return res
