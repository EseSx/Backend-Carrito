# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.ventas import sumarVenta, verVentas

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Ventas


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nueva venta ----
@router.post("/ingresar")
def ingresar_ventas(data: Ventas):
    """
    Registra una nueva venta en la base de datos.
    """
    res = sumarVenta(data)
    return res


# ---- Obtener todas las ventas ----
@router.get("/obtener")
def retornar_ventas():
    """
    Devuelve la lista de todas las ventas registradas.
    """
    res = verVentas()
    return res


# ---- Modificar venta existente ----
@router.post("/modificar")
def modificar_ventas():
    """
    Actualiza los datos de una venta específica.
    """
    return


# ---- Eliminar venta existente ----
@router.post("/eliminar")
def eliminar_ventas():
    """
    Elimina una venta de la base de datos.
    """
    return
