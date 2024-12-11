from dataclasses import dataclass, field
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''
@dataclass
class SubCantidad:
    SubQty: float 
    SubCod: str
    codigo: str 
