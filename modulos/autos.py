import psycopg2

dns = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"
conexionViajes = psycopg2.connect(dns)
cursor = conexionViajes.cursor()


def agregarAuto(auto_id, modelo, disponibles, precio_por_dia):
    cursor.execute(
        "INSERT INTO autos (auto_id, modelo, disponibles, precio_por_dia) VALUES(%s,%s,%s,%s)",
        (auto_id, modelo, disponibles, precio_por_dia),
    )
    conexionViajes.commit()

    return {"mensaje": "Nuevo auto cargado exitosamente"}


def borrarAuto(auto_id):
    cursor.execute("DELETE FROM autos WHERE auto_id = %s", (auto_id,))

    return {"Mensaje": "Auto eliminado exitosamente"}


print(agregarAuto(1, "Fiat 600", 20, 10000))
print(agregarAuto(2, "Ferrari", 15, 100000))
print(agregarAuto(3, "Fiat Duna", 10, 15000))
