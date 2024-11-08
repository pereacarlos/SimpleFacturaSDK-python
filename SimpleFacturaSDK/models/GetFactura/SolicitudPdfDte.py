class SolicitudPdfDte:
    def __init__(self, credenciales, dte_referenciado_externo):
        self.credenciales = credenciales
        self.dte_referenciado_externo = dte_referenciado_externo

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "dteReferenciadoExterno": self.dte_referenciado_externo.to_dict()
        }
