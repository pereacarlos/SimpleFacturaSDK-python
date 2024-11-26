from enum import Enum

class TipoSobreEnvio(Enum):
    AlSII = 0
    AlReceptor = 1

    def description(self):
        descriptions = {
            0: "Al SII",
            1: "Al Receptor"
        }
        return descriptions.get(self.value, "")