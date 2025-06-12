# --- Conexion con la BD ---
from main import cursor


# --- CRUD ---
# Insert Auto
def agregarAuto(auto_id, modelo, disponibles, precio_por_dia):
    cursor.execute(
        "INSERT INTO autos (auto_id, modelo, disponibles, precio_por_dia) VALUES(%s,%s,%s,%s)",
        (auto_id, modelo, disponibles, precio_por_dia),
    )
    cursor.commit()

    return {"mensaje": "Nuevo auto cargado exitosamente"}


# Delete Auto
def borrarAuto(auto_id):
    cursor.execute("DELETE FROM autos WHERE auto_id = %s", (auto_id,))

    return {"Mensaje": "Auto eliminado exitosamente"}


# Update / Read Auto
