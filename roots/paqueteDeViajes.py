# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.paqueteDeViajes import (
    agregarPaquetedeViaje,
    verPaquetedeViajes,
    quitarPaquetedeViaje,
)

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Paquete_de_viaje, CodigoPauqueteDeViaje


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nuevo paquete de viaje ----
@router.post("/ingresar")
def ingresar_paquetesDeViaje(data: Paquete_de_viaje):
    """
    Recibe datos para un nuevo paquete de viaje y lo agrega a la base de datos.
    """
    res = agregarPaquetedeViaje(data)
    return res


# ---- Obtener todos los paquetes de viaje ----
@router.get("/obtener")
def retornar_paquetesDeViaje():
    """
    Devuelve la lista de todos los paquetes de viaje almacenados.
    """
    res = verPaquetedeViajes()
    return res


# ---- Modificar paquete de viaje existente ---
@router.post("/modificar")
def modificar_paquetesDeViaje():
    """
    Actualiza los datos de un paquete de viaje existente.
    """
    return


# ---- Eliminar paquete de viaje por código ----
@router.post("/eliminar")
def eliminar_paquetesDeViaje(data: CodigoPauqueteDeViaje):
    """
    Elimina un paquete de viaje dado su código identificador.
    """
    res = quitarPaquetedeViaje(data)
    return res
