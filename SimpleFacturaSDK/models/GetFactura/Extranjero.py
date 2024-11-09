from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import Paises

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''


@dataclass
class Extranjero:
    NumId : str = ""
    Nacionalidad: Paises = Paises.NotSet

    _id: str = field(default="", init=False,metadata={"max_length": 20})

    def __post_init__(self):
        self._id = truncate(self.NumId, 20)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NumId=data.get('NumId'),
            Nacionalidad=Paises(data.get('Nacionalidad'))
        )
