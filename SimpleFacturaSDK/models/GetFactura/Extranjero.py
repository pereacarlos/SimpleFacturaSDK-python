from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from SimpleFacturaSDK.enum.CodigosAduana import Paises

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''


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
        self.Nacionalidad = Paises.NotSet
