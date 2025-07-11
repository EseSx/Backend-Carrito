# ===============================
#       Conexión con la Base de Datos
# ===============================

from main import get_connection

# ===============================
#     funciones auxiliares
# ===============================

from controladores.hashing import hash_password, verify_password
import bcrypt

# ===============================
#             CRUD
# ===============================


# ---- Crear nuevo cliente ----
def crearCliente(data):
    """
    Inserta un nuevo cliente en la tabla usuario_comun.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT MAX(uc_id) FROM usuario_comun")
        max_id = cur.fetchone()
        if max_id[0] is None:
            max_id = 1
        else:
            max_id = int(max_id[0]) + 1

        contraseñaHasheada = hash_password(data.contraseña)
        cur.execute(
            "INSERT INTO usuario_comun (uc_id, nombre, apellido, contraseña, correo_electronico) VALUES(%s,%s,%s,%s,%s)",
            (
                max_id,
                data.nombre,
                data.apellido,
                contraseñaHasheada,
                data.correo_electronico,
            ),
        )
        conn.commit()

        return {"Mensaje": "Se ha cargado un nuevo cliente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Ver todos los clientes ----
def verClientes():
    """
    Recupera todos los clientes de la base de datos.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM usuario_comun")
        respuesta = cur.fetchall()
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

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Eliminar cliente por ID ----
def eliminarUsuario(data):
    """
    Elimina un usuario de la tabla usuario_comun por su ID.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM usuario_comun WHERE uc_Id = %s", (data.uc_id,))
        conn.commit()

        return {"Mensaje": "Se ha eliminado un usuario correctamente"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Ver cliente por ID ----
def verClienteId(data):
    """
    Busca un cliente por su ID y devuelve sus datos.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM usuario_comun WHERE uc_id = %s", (data.uc_id,))
        respuesta = cur.fetchall()
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

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Validar cliente ----
def validarCliente(data):
    """
    Valida un cliente al volver a ingresar a la pagina
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT contraseña, correo_electronico FROM usuario_comun")
        res = cur.fetchall()
        for i in res:
            if data.usuarioIngresado == i[1]:
                hash_guardado = i[0]
                hash_guardado_bytes = hash_guardado.encode("utf-8")
                validacion = verify_password(
                    data.contraseñaIngresada, hash_guardado_bytes
                )

                return validacion

        return "Correo electronico incorrecto"

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()


# ---- Validar Admin ----
def validarAdmin(data):
    """
    Valida un administrador al volver a ingresar a la pagina
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT contraseña, correo_electronico FROM usuario_administrativo")
        res = cur.fetchall()
        for i in res:
            if data.usuarioIngresado == i[1]:
                hash_guardado = i[0]
                hash_guardado_bytes = hash_guardado.encode("utf-8")
                validacion = verify_password(
                    data.contraseñaIngresada, hash_guardado_bytes
                )

                return validacion

        return "Correo electronico incorrecto"

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cur.close()
        conn.close()
