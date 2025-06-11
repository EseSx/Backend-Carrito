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
