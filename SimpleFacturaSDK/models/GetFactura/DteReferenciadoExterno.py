from dataclasses import dataclass

@dataclass
class DteReferenciadoExterno:
    def __init__(self, folio, codigo_tipo_dte, ambiente):
        self.Folio = folio
        self.CodigoTipoDte = codigo_tipo_dte
        self.Ambiente = ambiente

    def to_dict(self):
        return {
            "folio": self.Folio,
            "codigoTipoDte": self.CodigoTipoDte,
            "ambiente": self.Ambiente
        }





