# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import cursor

# ===============================
#             CRUD
# ===============================


# ---- Crear nuevo cliente ----
def crearCliente(data):
    """
    Inserta un nuevo cliente en la tabla usuario_comun.
    """
    cursor.execute(
        "INSERT INTO usuario_comun (nombre, apellido, contraseña, correo_electronico) VALUES(%s,%s,%s,%s)",
        (data.nombre, data.apellido, data.contraseña, data.correo_electronico),
    )
    cursor.commit()

    return {"Mensaje": "Se ha cargado un nuevo cliente"}


# ---- Ver todos los clientes ----
def verClientes():
    """
    Recupera todos los clientes de la base de datos.
    """
    cursor.execute("SELECT * FROM usuario_comun")
    respuesta = cursor.fetchall()
    usuarios = []
    for usuario in respuesta:
        dicConvertido = []
        dicConvertido.append(
            {
                "Usuario id": usuario[0],
                "Nombre": usuario[1],
                "Apellido": usuario[2],
                "Contraseña": usuario[3],
                "Email": usuario[4],
            }
        )

        usuarios.append(dicConvertido)

    return usuarios


# ---- Eliminar cliente por ID ----
def eliminarUsuario(uc_id):
    """
    Elimina un usuario de la tabla usuario_comun por su ID.
    """
    cursor.execute("DELETE FROM usuario_comun WHERE uc_Id = %s", (uc_id,))
    cursor.commit()

    return {"Mensaje": "Se ha eliminado un usuario correctamente"}


# ---- Ver cliente por ID ----
def verClienteId(uc_id):
    """
    Busca un cliente por su ID y devuelve sus datos.
    """
    cursor.execute("SELECT * FROM usuario_comun WHERE uc_id = %s", (uc_id,))
    respuesta = cursor.fetchall()
    dicConvertido = []
    dicConvertido.append(
        {
            "Usuario id": respuesta[0][0],
            "Nombre": respuesta[0][1],
            "Apellido": respuesta[0][2],
            "Contraseña": respuesta[0][3],
            "Email": respuesta[0][4],
        }
    )

    return dicConvertido
