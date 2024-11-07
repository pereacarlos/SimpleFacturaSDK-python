from enum import Enum

class AmbienteEnum(Enum):
    Certificacion = (0, "Certificación")
    Produccion = (1, "Producción")

    @property
    def code(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
