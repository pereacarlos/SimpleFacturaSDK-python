from enum import Enum
import json

class TipoEnvioLibroEnum(Enum):
    NotSet = ("")
    Total = 1
    Parcial = 2
    Final = 3
    Ajuste = 4

    def description(self):
        descriptions = {
            "": "",
            1: "TOTAL",
            2: "PARCIAL",
            3: "FINAL",
            4: "AJUSTE"
        }
        return descriptions.get(self.value, "")