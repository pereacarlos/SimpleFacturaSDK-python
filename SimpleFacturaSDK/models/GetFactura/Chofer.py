from dataclasses import dataclass, field

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Chofer:
    RUTChofer: str = ''
    NombreChofer: str = ''

    __nombre: str = field(default="", metadata={"max_length": 30})

    def __post_init__(self):
        self.__nombre = truncate(self.NombreChofer, 30)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            RUTChofer=data.get('RUTChofer'),
            NombreChofer=data.get('NombreChofer')
        )
