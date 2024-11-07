from enum import Enum

class TipoSobreEnvio(Enum):
    AlSII = (0, "Al SII")
    AlReceptor = (1, "Al Receptor")

    @property
    def description(self):
        return self.value[1]
