from dataclasses import dataclass

@dataclass
class ActividadesEconomicaEnt:
    codigo: int = 0 
    descripcion: str = "" 

    @classmethod
    def from_dict(cls, data):
        return cls(
            codigo=data.get("codigo", 0),
            descripcion=data.get("descripcion", "") 
        )
