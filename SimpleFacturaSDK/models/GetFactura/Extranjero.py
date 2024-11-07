from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

# Definir la enumeración para los países
class Paises(Enum):
    NotSet = 0
    # Agregar otros códigos de países según sea necesario

@dataclass
class Extranjero:
    Nacionalidad: Paises = Paises.NotSet

    _id: str = field(default="", init=False)

    @property
    def NumId(self) -> str:
        return self._id

    @NumId.setter
    def NumId(self, value: str):
        self._id = truncate(value, 20)


    def __init__(self):
        self.NumId = ''
        self.Nacionalidad = Paises.NOT_SET
