from dataclasses import dataclass

@dataclass
class Retenedor:
    IndAgente: str 
    MntBaseFaena: int 
    MntMargComer: int 
    PrcConsFinal: int 

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            IndAgente=data.get('IndAgente'),
            MntBaseFaena=data.get('MntBaseFaena'),
            MntMargComer=data.get('MntMargComer'),
            PrcConsFinal=data.get('PrcConsFinal')
        )