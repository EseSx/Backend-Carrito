# La tabla que maneja este crud es Ventas
import psycopg2


# Convertir a diccionario los datos de la Tabla Ventas
def convertirDatosVentas(respuesta):
    dicConvertido = []
    for item in respuesta:
        dicConvertido.append(
            {
                "ID": item[0],
                "Fecha": item[1],
                "Hora": item[2],
                "Medio de pago": item[3],
                "Cuotas": item[4],
                "Cantidad": item[5],
            }
        )

        return dicConvertido


# def verVentas(respuesta):
# En la tabla Ventas
# cursor.execute("SELECT * FROM ventas")
# respuesta = cursor.execute.fetchall()

# nrepuesta = convertirDatos(respuesta)

# return nrepuesta
