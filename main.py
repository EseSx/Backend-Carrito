# ==============================================
#            Creación de la aplicación
# ==============================================

from fastapi import FastAPI

app = FastAPI()

# ==============================================
#           Configuración de CORS
# ==============================================

from fastapi.middleware.cors import CORSMiddleware

# Permitir solicitudes desde cualquier origen
# (Recuerda restringir antes de producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,  # Permitir el uso de cookies/autenticación
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# ==============================================
#    Conexión/Creación de la base de datos
# ==============================================

import psycopg


# URL de conexión a la base de datos PostgreSQL
hostURL = "postgresql://santi:NfWdr3CRaZ9q3qZhazSVltB0dW3qQ52W@dpg-d13hpvggjchc73cb6fj0-a.ohio-postgres.render.com/bd_productos"

conexion = psycopg.connect(hostURL)

cursor = conexion.cursor()


# ==============================================
#                  Rutas
# ==============================================

# Importar y registrar todos los routers de tu proyecto
from roots.autos import router as autos_routers
from roots.clientes import router as clientes_routers
from roots.excursiones import router as excursiones_routers
from roots.paqueteDeViajes import router as paqueteDeViajes_routers
from roots.ventas import router as ventas_routers
from roots.viajes import router as viajes_routers

# Registrar routers con prefijos
app.include_router(autos_routers, prefix="/autos")
app.include_router(clientes_routers, prefix="/clientes")
app.include_router(excursiones_routers, prefix="/excursiones")
app.include_router(paqueteDeViajes_routers, prefix="/paqueteDeViajes")
app.include_router(ventas_routers, prefix="/ventas")
app.include_router(viajes_routers, prefix="/viajes")
