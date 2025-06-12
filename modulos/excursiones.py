# --- Conexion BD ---
from main import cursor


# --- CRUD ---
# Insert Excursiones
def agregarExcursiones(excursion_id, nombre, inicio, final, descripcion, lugar):
    cursor.execute(
        "INSERT INTO excursiones (excursion_id, nombre, inicio, final, descripcion, lugar) VALUES(%s,%s,%s,%s,%s,%s)",
        (excursion_id, nombre, inicio, final, descripcion, lugar),
    )
    cursor.commit()

    return {"Mensaje": "Se ha agregado la excursion exitosamente"}


# Delete Excursiones
def eliminarExcursion(excursion_id):
    cursor.execute("DELETE FROM excursiones WHERE excursion_id = %s", (excursion_id,))
    cursor.commit()

    return {"Mensaje": "Borrado exitosamente"}


# --- Relacionar excursiones & paquetes de viaje ---
def paqueteViajesExcursion(pv_id, exc_id):
    cursor.execute("INSERT INTO pv_exc (pv_id, exc_id) VALUES (%s,%s)", (pv_id, exc_id))
    cursor.commit()

    return {"Mensaje": "Se ha vinculado una excursion con un paquete de viajes"}


# --- Query de excursiones ---
def buscarExcursionporId(excursion_id):
    cursor.execute("SELECT * FROM excursiones WHERE excursion_id = %s", (excursion_id,))
    respuesta = cursor.fetchall()
    dicExcursiones = []

    inicio = respuesta[0][2]
    inicio = inicio.strftime("%H:%M:%S")
    final = respuesta[0][3]
    final = final.strftime("%H:%M:%S")

    dicExcursiones.append(
        {
            "Excursion id": respuesta[0][0],
            "Nombre": respuesta[0][1],
            "Inicio": inicio,
            "Final": final,
            "Descripcion": respuesta[0][4],
            "Lugar": respuesta[0][5],
        }
    )

    return dicExcursiones
