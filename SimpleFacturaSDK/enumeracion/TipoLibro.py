from enum import Enum


class TipoLibroEnum(Enum):
    NotSet = 0
    Mensual = 1
    Especial = 2
    Rectifica = 3

    def description(self):
        descriptions = {
            0: "",
            1: "MENSUAL",
            2: "ESPECIAL",
            3: "RECTIFICA"
        }
        return descriptions.get(self.value, "")

class TipoLibroOrigenEnum(Enum):
    NotSet = 0
    IECV = 1
    Boletas = 2
    Guias = 3

    def description(self):
        descriptions = {
            0: "",
            1: "IECV",
            2: "BOLETAS",
            3: "GUIAS"
        }
        return descriptions.get(self.value, "")

