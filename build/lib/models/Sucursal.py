from dataclasses import dataclass

@dataclass
class Sucursal:
    nombre: str
    direccion: str

    def __init__(self, nombre: str, direccion: str = None):
        self.nombre = nombre
        self.direccion = direccion
