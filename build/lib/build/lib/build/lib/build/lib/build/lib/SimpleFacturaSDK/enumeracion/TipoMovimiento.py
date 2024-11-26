from enum import Enum

class TipoMovimientoEnum(Enum):
    NotSet = ("")
    Descuento = ("D")
    Recargo = ("R")

    def description(self):
        descriptions = {
            "": "",
            "D": "D",
            "R": "R"
        }
        return descriptions.get(self.value, "")