# --- Creacion de la app ---
from fastapi import FastAPI

app = FastAPI()

# --- Creacion del CORS ---
from fastapi.middleware.cors import CORSMiddleware

# Permite solicitudes desde cualquier origen (Modificar pre-lanzamiento)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,  # Permitir el uso de cookies/autenticación
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# --- Creacion de modelos pydantic ---
from pydantic import BaseModel


class Producto(BaseModel):
    """
    Modelo para recibir un producto
    """

    nombre: str
    codigo: str
    descripcion: str
    precio: str
    stock: int


class Usuarios(BaseModel):
    """
    Modelo para recibir usuarios
    """

    username: str
    password: str
    # Forma de nivel de acceso que diferencie entre usuario comun y administrador para diferirlo entre Bases de datos
    # Ej: accessLevel: int / Si nivel de acceso es mayor a 1 entonces el usuario se registra con una clave de nivel admin


@app.post("/Ingresar_Producto")
async def Ingresar_Producto(data: Producto):
    """
    Ingresa el producto a la base de datos pertinente.

    Args:
        data (Producto): Objeto con los datos de los productos.

    Returns:
        Dict: Mensaje de confirmacion de ingreso de producto.
    """
    # Pasar a cualquier base de datos que reciba los objetos
    # Resultado = await ingresadorProducto(data)
    # return {
    #   "respuesta": "El productro se guardo con exito"
    #   "Corroboracion": f"Este es su producto? {data}"
    # }


# --- Coneccion de base de datos ---
import psycopg2

hostURL = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"

conneccion = psycopg2.connect(hostURL)

cursor = conneccion.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS  (codigo TEXT, nombre TEXT, descripcion TEXT, precio REAL, stock int, PRIMARY KEY (codigo))
    """
)

cursor.execute(
    """
    INSERT INTO Viajes (codigo, nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s, %s)
    """,
    ("123.456.Cordoba", "Cordoba", "Viaje a Cordoba", 120000.99, 90),
)

# --- Codificado de Bcript ---
import bcrypt

password = "mi_contraseña_segura".encode("utf-8")

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Contraseña original:", password)
print("Hash generado:", hashed)

entrada_usuario = "mi_contraseña_segur".encode("utf-8")

if bcrypt.checkpw(entrada_usuario, hashed):
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
