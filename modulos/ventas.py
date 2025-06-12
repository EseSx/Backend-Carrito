# --- Conexion con la BD ---
from main import cursor


# --- Convertir datos ventas a diccionarion ---
def convertirDatosVentas(respuesta):

    registros = []
    for registro in respuesta:
        dicConvertido = []
        fecha = registro[1]
        fecha = fecha.strftime("%Y-%m-%d")
        hora = registro[2]
        hora = hora.strftime("%H:%M:%S")

        if registro[6]:
            codigo_de_viaje = registro[6]
            tipo = "Viaje Simple"
        else:
            codigo_de_viaje = registro[7]
            tipo = "Paquete de Viaje"
        dicConvertido.append(
            {
                "Id Venta": registro[0],
                "Fecha": fecha,
                "Hora": hora,
                "Medio de pago": registro[3],
                "Cuotas": registro[4],
                "Cantidad": registro[5],
                "Codigo de viaje": codigo_de_viaje,
                "Tipo": tipo,
                "Precio": registro[8],
            }
        )
        registros.append(dicConvertido)

    return registros


# --- CRUD ---
# Read ventas
def verVentas():

    cursor.execute("SELECT * FROM ventas")
    respuesta = cursor.fetchall()
    nrespuesta = convertirDatosVentas(respuesta)

    return nrespuesta


# Create venta
from controladores.date import convertirDate, convertirHora


def sumarVenta(
    vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio
):
    fecha = convertirDate(fecha)
    hora = convertirHora(hora)
    cursor.execute(
        "INSERT INTO ventas (vtas_id, fecha, hora, medio_de_pago, cuotas, cantidad, codigo_vs, codigo_pv, precio) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            vtas_id,
            fecha,
            hora,
            medio_de_pago,
            cuotas,
            cantidad,
            codigo_vs,
            codigo_pv,
            precio,
        ),
    )
    cursor.commit()

    return {"Mensaje": "Venta sumada"}


# --- Query venta ---
def buscarVentaId(vtas_id):

    cursor.execute("SELECT * FROM ventas WHERE vtas_id = %s", (vtas_id,))
    registro = cursor.fetchall()
    dicConvertido = []
    fecha = registro[0][1]
    fecha = fecha.strftime("%Y-%m-%d")
    hora = registro[0][2]
    hora = hora.strftime("%H:%M:%S")

    if registro[0][6]:
        codigo_de_viaje = registro[0][6]
        tipo = "Viaje Simple"
    else:
        codigo_de_viaje = registro[0][7]
        tipo = "Paquete de Viaje"

    dicConvertido.append(
        {
            "Id Venta": registro[0][0],
            "Fecha": fecha,
            "Hora": hora,
            "Medio de pago": registro[0][3],
            "Cuotas": registro[0][4],
            "Cantidad": registro[0][5],
            "Codigo de viaje": codigo_de_viaje,
            "Tipo": tipo,
            "Precio": registro[0][8],
        }
    )

    return dicConvertido


# --- Incompelto ---
def cancelarCompra(vtas_id):
    venta = buscarVentaId(vtas_id)
