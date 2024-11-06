class DteReferenciadoExterno:
    def __init__(self, folio, codigo_tipo_dte, ambiente):
        self.Folio = folio
        self.CodigoTipoDte = codigo_tipo_dte
        self.Ambiente = ambiente

    def to_dict(self):
        return {
            "Folio": self.Folio,
            "CodigoTipoDte": self.CodigoTipoDte,
            "Ambiente": self.Ambiente
        }
