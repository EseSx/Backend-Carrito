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

# --- Coneccion/Creacion de base de datos ---
import psycopg2

hostURL = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"

conexion = psycopg2.connect(hostURL)

cursor = conexion.cursor()


# --- Rutas ---
from roots import rutas

for router in rutas:
    app.include_router(router)
