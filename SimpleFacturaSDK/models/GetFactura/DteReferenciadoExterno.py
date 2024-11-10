from dataclasses import dataclass

@dataclass
class DteReferenciadoExterno:
    Folio: int
    CodigoTipoDte: int
    Ambiente: str
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            folio=data.get("Folio"),
            codigo_tipo_dte=data.get("CodigoTipoDte"),
            ambiente=data.get("Ambiente")
        )

    def to_dict(self):
        return {
            "Folio": self.Folio,
            "CodigoTipoDte": self.CodigoTipoDte,
            "Ambiente": self.Ambiente
        }
