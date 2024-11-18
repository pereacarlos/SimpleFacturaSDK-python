from dataclasses import dataclass, field
from typing import Optional
from enumeracion.CodigosAduana import Paises

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''


@dataclass
class Extranjero:
    NumId : str 
    Nacionalidad: Paises 