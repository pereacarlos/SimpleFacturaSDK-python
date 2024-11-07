from dataclasses import dataclass, field

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Chofer:
    RUTChofer: str = ''
    _nombre: str = field(default="", init=False)

    @property
    def NombreChofer(self) -> str:
        return self._nombre

    @NombreChofer.setter
    def NombreChofer(self, value: str):
        self._nombre = truncate(value, 30)


    def __init__(self):
        self.RUTChofer = ''
        self.NombreChofer = ''
