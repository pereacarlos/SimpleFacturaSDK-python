from dataclasses import dataclass

@dataclass
class ActividadesEconomicaEnt:
    codigo: int = 0  # Valor predeterminado
    descripcion: str = ""  # Valor predeterminado vacío

    @classmethod
    def from_dict(cls, data):
        return cls(
            codigo=data.get("codigo", 0),  # Obtiene el valor de "codigo" o usa 0 si falta
            descripcion=data.get("descripcion", "")  # Obtiene el valor de "descripcion" o usa una cadena vacía si falta
        )

'''
from dataclasses import dataclass

@dataclass
class ActividadeconomicaApiEnt:
    Codigo: int
    Descripcion: str = ""

    def __init__(self, Codigo: int, Descripcion: str = ""):
        self.Codigo = Codigo
        self.Descripcion = Descripcion'''