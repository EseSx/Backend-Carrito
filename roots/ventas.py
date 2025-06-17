# ===============================
#         Creación del Router
# ===============================

from fastapi import APIRouter

router = APIRouter()

# ===============================
#       Importación de CRUD
# ===============================

from modulos.ventas import (
    sumarVenta,
    verVentas,
    buscarVentaId,
    cancelarCompraTVS,
    buscarVentaUsuario,
)

# ===============================
#       Importación de Modelos
# ===============================

from modulos.esquemas import Venta_request, Venta_id, Usuarios_comunes_id

# ===============================
#       Funciones auxiliares
# ===============================

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from fastapi.responses import JSONResponse

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


# ---- Obtener todas las ventas relacionadas a una id ----
@router.post("/obtenerID")
def retornar_ventas(data: Venta_id):
    """
    Devuelve la lista de todas las ventas registradas por id.
    """
    res = buscarVentaId(data)
    return res


# ---- Obtener todas las ventas relacionadas a un usuario ----
@router.post("/obtenerUsuario")
def retornar_ventas(data: Usuarios_comunes_id):
    """
    Devuelve la lista de todas las ventas registradas por usuario.
    """
    res = buscarVentaUsuario(data)
    return res


# ---- Eliminar venta existente ----
@router.post("/eliminarTVS")
def eliminar_ventas(data: Venta_id):
    """
    Elimina una venta de la base de datos.
    """
    res = cancelarCompraTVS(data.vtas_id)
    return res


# ---- Confirmar mail para venta ----
@router.post("/confirmarMail")
def confirmar_mail(data: Venta_request):
    """
    Elimina una venta de la base de datos.
    """
    try:
        mensaje = f"""
        Hola 👋

        Gracias por tu compra en Horizon Air ✈️

        🧾 Detalles del viaje:
        * Código de viaje: {data.data.codigo_vs if data.data.codigo_vs is not None else data.data.codigo_pv}
        * Precio: ${data.data.precio}
        * Medio de pago: {data.data.medio_de_pago}
        * Forma de pago: {'{} cuotas'.format(data.data.cantidad) if data.data.cuotas else 'Pago único'}

        ¡Nos alegra acompañarte en esta aventura! 🌎

        El equipo de Horizon Air.
        """

        msg = MIMEMultipart()
        msg["From"] = "Horizon Air <pruebaOlimpiadas@gmail.com>"
        msg["To"] = data.correo_electronico
        msg["Subject"] = "🛫 Tu compra ha sido confirmada"
        msg.attach(MIMEText(mensaje, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("pruebaOlimpiadas@gmail.com", "zipw adno ybwt luqt")
            smtp.sendmail(msg["From"], msg["To"], msg.as_string())

        return {"success": True}

    except Exception as e:
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )
