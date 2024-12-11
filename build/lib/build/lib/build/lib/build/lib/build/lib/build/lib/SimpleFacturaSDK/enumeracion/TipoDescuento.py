from enum import Enum
class ExpresionDineroEnum(Enum):
    NotSet = ("")
    Porcentaje = ("%")
    Pesos = ("$")

    def description(self):
        descriptions = {
            "": "",
            "%": "%",
            "$": "$"
        }
        return descriptions.get(self.value, "")