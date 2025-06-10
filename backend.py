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


class Usuarios_comunes(BaseModel):
    """
    Modelo para recibir usuarios comunes
    """

    nombre: str
    apellido: str
    contraseña: str
    correo_electronico: str
    estatus: str


class Ventas(BaseModel):
    """
    Modelo para recibir ventas
    """

    medio_de_pago: str
    cuotas: bool
    cantidad: int
    codigo_viaje: int


class Viaje_simple(BaseModel):
    codigo: int
    nombre: str
    descripcion: str
    precio: float
    origen: str
    destino: str
    transporte: str
    fecha: str
    hora: str
    cupos: int
    duracion_aprox: str
    tipo_de_viaje: str  # solo ida o ida y vuelta


class Paquete_de_viaje(BaseModel):
    nombre: str
    precio: float
    origen: str
    destino: str
    estadia: str
    tipo: str  # nacional o internacional


class Auto(BaseModel):
    modelo: str
    disponibles: int
    precio_por_dia: float


class Excursiones(BaseModel):
    nombre: str
    inicio: str
    final: str


# --- Creacion de las rutas ---


# --- Coneccion/Creacino de base de datos ---
import psycopg2

hostURL = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"

conexion = psycopg2.connect(hostURL)

cursor = conexion.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuario_comun (
    uc_id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    correo_electronico TEXT NOT NULL);

    CREATE TABLE IF NOT EXISTS usuario_administrativo (
    ua_id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    contraseña TEXT NOT NULL,
    correo_electronico TEXT NOT NULL);

    CREATE TABLE IF NOT EXISTS viaje_simple (
    codigo INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL,
    origen TEXT NOT NULL,
    destino TEXT NOT NULL,
    transporte TEXT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    cupos INTEGER NOT NULL,
    duracion_aprox TEXT NOT NULL,
    tipo_de_viaje TEXT NOT NULL);

    CREATE TABLE IF NOT EXISTS paquete_de_viajes (
    codigo INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    origen TEXT NOT NULL,
    destino TEXT NOT NULL,
    estadia TEXT NOT NULL,
    tipo TEXT NOT NULL);

    CREATE TABLE IF NOT EXISTS ventas (
    vtas_id INTEGER PRIMARY KEY NOT NULL,
    fecha DATE NOT NULL,
    hora DATE NOT NULL,
    medio_de_pago TEXT NOT NULL,
    cuotas BOOLEAN NOT NULL,
    cantidad INTEGER,
    codigo_vs INTEGER,
    codigo_pv INTEGER,
    FOREIGN KEY (codigo_vs) REFERENCES viaje_simple(codigo),
    FOREIGN KEY (codigo_pv) REFERENCES paquete_de_viajes(codigo));
    
    CREATE TABLE IF NOT EXISTS vtas_uc (
    vtas_id INTEGER NOT NULL,
    uc_id INTEGER NOT NULL,
    FOREIGN KEY (vtas_id) REFERENCES ventas(vtas_id),
    FOREIGN KEY (uc_id) REFERENCES usuario_comun(uc_id));

    CREATE TABLE IF NOT EXISTS auto (
    auto_id INTEGER PRIMARY KEY NOT NULL,
    modelo TEXT NOT NULL,
    disponibles INTEGER NOT NULL,
    precio_por_dia REAL NOT NULL);

    CREATE TABLE IF NOT EXISTS vs_at (
    vs_id INTEGER NOT NULL,
    at_id INTEGER NOT NULL,
    FOREIGN KEY (vs_id) REFERENCES viaje_simple(codigo),
    FOREIGN KEY (at_id) REFERENCES auto(auto_id));


    CREATE TABLE IF NOT EXISTS excursiones (
    excursion_id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    inicio TIME NOT NULL,
    final TIME NOT NULL);

    CREATE TABLE IF NOT EXISTS pv_exc (
    pv_id INTEGER NOT NULL,
    exc_id INTEGER NOT NULL,
    FOREIGN KEY (pv_id) REFERENCES paquete_de_viajes(codigo),
    FOREIGN KEY (exc_id) REFERENCES excursiones(excursion_id));

    CREATE TABLE IF NOT EXISTS exc_at (
    pv_id INTEGER NOT NULL,
    at_id INTEGER NOT NULL,
    FOREIGN KEY (pv_id) REFERENCES paquete_de_viajes(codigo),
    FOREIGN KEY (at_id) REFERENCES auto(auto_id));
    """
)

conexion.commit()
conexion.close()

# --- Codificado de Bcript ---
import bcrypt

# password = "mi_contraseña_segura".encode("utf-8")

# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# print("Contraseña original:", password)
# print("Hash generado:", hashed)

# entrada_usuario = "mi_contraseña_segur".encode("utf-8")

# if bcrypt.checkpw(entrada_usuario, hashed):
#     print("Contraseña correcta")
# else:
#     print("Contraseña incorrecta")
