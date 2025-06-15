# ===============================
#   Creación de modelos Pydantic
# ===============================
from pydantic import BaseModel
from typing import Optional


class Usuarios_comunes(BaseModel):
    """
    Modelo Pydantic para la creación de usuarios comunes.
    """

    nombre: str
    apellido: str
    contraseña: str
    correo_electronico: str


class Usuarios_comunes_id(BaseModel):
    """
    Modelo Pydantic para obtener la id de un usuario comun.
    """

    uc_id: int


class Ventas(BaseModel):
    """
    Modelo Pydantic para registrar información de una venta.
    """

    medio_de_pago: str
    cuotas: bool
    cantidad: int
    codigo_vs: Optional[int] = None
    codigo_pv: Optional[int] = None
    precio: float


class Venta_request(BaseModel):
    """
    Modelo Pydantic para registrar información de una venta y relacionarlo a un usuario.
    """

    data: Ventas
    correo_electronico: str


class Venta_id(BaseModel):
    """
    Modelo Pydantic para obtener la id de una venta.
    """

    vtas_id: int


class Viaje_simple(BaseModel):
    """
    Modelo Pydantic para representar un viaje simple.
    """

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


class Viaje_simple_id(BaseModel):
    """
    Modelo Pydantic para representar la ID de un viaje simple.
    """

    vs_id: int


class Paquete_de_viaje(BaseModel):
    """
    Modelo Pydantic para representar un paquete de viaje.
    """

    nombre: str
    precio: float
    origen: str
    destino: str
    estadia: str
    tipo: str  # Valores: 'solo ida' o 'ida y vuelta'
    descripcion: str
    cupos: int
    duracion: str
    tipo_de_viaje: str  # Valores: 'nacional' o 'internacional'
    hora: str  # Formato recomendado: 'HH:MM'
    fecha: str  # Formato recomendado: 'dd/mm/yy'


class Codigo_paquete_de_viaje(BaseModel):
    """
    Modelo Pydantic para obtener el codigo de un paquete de viaje
    """

    codigoDeViaje: int


class Paquete_de_viaje_id(BaseModel):
    """
    Modelo Pydantic para representar la id de un paquete de viaje.
    """

    pv_id: int


class Auto(BaseModel):
    """
    Modelo Pydantic para representar un auto disponible para alquiler.
    """

    modelo: str
    disponibles: int
    precio_por_dia: float


class Auto_id(BaseModel):
    """
    Modelo Pydantic para representar el id de un auto.
    """

    auto_id: int


class Vinculo_vs_a_auto(BaseModel):
    """
    Modelo Pydantic para representar el vinculo de un viaje simple a un auto
    """

    vs_id: int
    at_id: int


class Vinculo_pv_a_auto(BaseModel):
    """
    Modelo Pydantic para representar el vinculo de un paquete de viajes a un auto
    """

    pv_id: int
    at_id: int


class Excursiones(BaseModel):
    """
    Modelo Pydantic para representar una excursión.
    """

    nombre: str
    inicio: str  # Hora de inicio (se recomienda formato 'HH:MM')
    final: str  # Hora de finalización (se recomienda formato 'HH:MM')
    descripcion: str
    lugar: str


class Excursiones_id(BaseModel):
    """
    Modelo Pydantic para representar la ID de una Excursion.
    """

    excursion_id: int


class Vinculo_pv_a_exc(BaseModel):
    """
    Modelo Pydantic para representar el vinculo de un paquete de viaje a una excursion.
    """

    pv_id: int
    exc_id: int
