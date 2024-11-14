from enum import Enum

class IndicadorSinCostoEnum(Enum):
    NotSet = 0
    VentaSinCosto = 1

    def description(self):
        descriptions = {
            0: "",
            1: "1"
        }
        return descriptions.get(self.value, "")
   