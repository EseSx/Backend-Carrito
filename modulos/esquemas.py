# ===============================
#   Creación de modelos Pydantic
# ===============================
from pydantic import BaseModel


class Usuarios_comunes(BaseModel):
    """
    Modelo Pydantic para la creación de usuarios comunes.
    """

    nombre: str
    apellido: str
    contraseña: str
    correo_electronico: str
    estatus: str


class Ventas(BaseModel):
    """
    Modelo Pydantic para registrar información de una venta.
    """

    medio_de_pago: str
    cuotas: bool
    cantidad: int
    codigo_vs: int
    codigo_pv: int
    precio: float


class Viaje_simple(BaseModel):
    """
    Modelo Pydantic para representar un viaje simple.
    """

    codigo: int
    nombre: str
    descripcion: str
    precio: float
    origen: str
    destino: str
    transporte: str
    fecha: str  # Formato recomendado: 'dd/mm/yy'
    hora: str  # Formato recomendado: 'HH:MM'
    cupos: int
    duracion_aprox: str
    tipo_de_viaje: str  # Valores: 'solo ida' o 'ida y vuelta'
    estado: str


class Paquete_de_viaje(BaseModel):
    """
    Modelo Pydantic para representar un paquete de viaje.
    """

    nombre: str
    precio: float
    origen: str
    destino: str
    estadia: str
    tipo: str  # Valores: 'nacional' o 'internacional'
    estado: str


class Auto(BaseModel):
    """
    Modelo Pydantic para representar un auto disponible para alquiler.
    """

    auto_id: int
    modelo: str
    disponibles: int
    precio_por_dia: float


class Excursiones(BaseModel):
    """
    Modelo Pydantic para representar una excursión.
    """

    nombre: str
    inicio: str  # Fecha de inicio (se recomienda formato 'dd/mm/yy')
    final: str  # Fecha de finalización (se recomienda formato 'dd/mm/yy')
    descripcion: str
    lugar: str
