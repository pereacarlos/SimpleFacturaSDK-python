from enum import Enum


class TipoRecargoComisionEnum(Enum):
    NotSet = ("")
    Comision = ("C")
    OtrosCargos = ("O")

    def description(self):
        descriptions = {
            "": "",
            "C": "C",
            "O": "O"
        }
        return descriptions.get(self.value, "")
