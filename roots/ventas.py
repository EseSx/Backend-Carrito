# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.ventas import sumarVenta, verVentas, buscarVentaId, cancelarCompraTVS

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Venta_request, Venta_id


# ===============================
#           Rutas CRUD
# ===============================


# ---- Crear nueva venta ----
@router.post("/ingresar")
def ingresar_ventas(data: Venta_request):
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


# ---- Obtener todas las ventas ----
@router.post("/obtenerID")
def retornar_ventas(data: Venta_id):
    """
    Devuelve la lista de todas las ventas registradas por id.
    """
    res = buscarVentaId(data)
    return res


# ---- Eliminar venta existente ----
@router.post("/eliminarTVS")
def eliminar_ventas(data: Venta_id):
    """
    Elimina una venta de la base de datos.
    """
    res = cancelarCompraTVS(data.vtas_id)
    return res
