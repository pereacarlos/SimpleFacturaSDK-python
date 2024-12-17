from dataclasses import dataclass

@dataclass
class DteReferenciadoExterno:
    folio: int
    codigoTipoDte: int
    ambiente: int


    def to_dict(self):
        return {
            "folio": self.folio,
            "codigoTipoDte": self.codigoTipoDte,
            "ambiente": self.ambiente
        }





