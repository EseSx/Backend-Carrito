# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#         Importación de CRUD
# ===============================

from modulos.autos import agregarAuto, borrarAuto, vinculaVSaAuto


# ===============================
#         Importación de Modelos
# ===============================

from modulos.esquemas import Auto, AutoID, VinculoVSaAuto


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


# ---- Obtener lista de autos ----
@router.get("/obtener")
async def retornar_autos():
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    return


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
