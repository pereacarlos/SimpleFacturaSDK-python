from dataclasses import dataclass

@dataclass
class TrazasEnt:
    fecha: str
    descripcion: str

    def __init__(self, fecha: str, descripcion: str):
        self.fecha = fecha
        self.descripcion = descripcion