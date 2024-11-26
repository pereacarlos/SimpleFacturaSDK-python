from dataclasses import dataclass, field

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Chofer:
    RUTChofer: str 
    NombreChofer: str 