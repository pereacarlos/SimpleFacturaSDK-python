from enum import Enum

class TipoCertificadoEnum(Enum):
    NotSet = ("")
    Certificacion = ("Certificación")
    Produccion = ("Producción")
    @property
    def description(self):
        return self.value[0]
