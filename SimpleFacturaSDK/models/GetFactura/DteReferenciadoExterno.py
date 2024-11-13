from dataclasses import dataclass

@dataclass
class DteReferenciadoExterno:
    Folio: int
    CodigoTipoDte: int
    Ambiente: int


    def to_dict(self):
        return {
            "folio": self.Folio,
            "codigoTipoDte": self.CodigoTipoDte,
            "ambiente": self.Ambiente
        }





