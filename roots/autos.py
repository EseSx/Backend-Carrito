# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#         Importación de CRUD
# ===============================

from modulos.autos import agregarAuto, borrarAuto


# ===============================
#         Importación de Modelos
# ===============================

from modulos.esquemas import Auto


# ===============================
#             Rutas CRUD
# ===============================


# ---- Crear nuevo auto ----
@router.post("/ingresar")
def ingresar_autos(data: Auto):
    """
    Recibe los datos de un auto y llama a la función para agregarlo a la base.
    """
    agregarAuto(data)
    return


# ---- Obtener lista de autos ----
@router.get("/obtener")
def retornar_autos():
    """
    Devuelve la lista de autos almacenados (pendiente implementación).
    """
    return


# ---- Modificar datos de un auto ----
@router.post("/modificar")
def modificar_autos():
    """
    Actualiza los datos de un auto existente (pendiente implementación).
    """
    return


# ---- Eliminar un auto por ID ----
@router.post("/eliminar")
def eliminar_autos(auto_id):
    """
    Elimina un auto de la base de datos utilizando su ID.
    """
    borrarAuto(auto_id)
    return
