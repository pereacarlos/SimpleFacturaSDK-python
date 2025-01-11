from dataclasses import dataclass

@dataclass
class Usuario:
    rut: str
    nombre: str
    apellidos: str
    email: str

    def __init__(self, rut: str, nombre: str, apellidos: str, email: str):
        self.rut = rut
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
