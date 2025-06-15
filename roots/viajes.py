# ===============================
#       Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.viajeSimple import verViajesSimples, agregarViajeSimple, quitarViajesimple

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Viaje_simple, Viaje_simple_id


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear viaje simple ----
@router.post("/ingresar")
def ingresar_viaje_simple(data: Viaje_simple):
    """
    Registra un nuevo viaje simple en la base de datos.
    """
    res = agregarViajeSimple(data)
    return res


# ---- Obtener todos los viajes simples ----
@router.get("/obtener")
def retornar_viaje_simple():
    """
    Devuelve la lista de todos los viajes simples registrados.
    """
    return verViajesSimples()


# ---- Eliminar viaje simple ----
@router.post("/eliminar")
def eliminar_viaje_simple(data: Viaje_simple_id):
    """
    Elimina un viaje simple de la base de datos usando su código.
    """
    res = quitarViajesimple(data.vs_id)
    return res
