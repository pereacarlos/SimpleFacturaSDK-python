from enum import Enum
import json

class TipoCuentaPagoEnum(Enum):
    NotSet = ("")
    CuentaCorriente = ("CORRIENTE")
    Ahorro = ("AHORRO")
    Vista = ("VISTA")
    Otro = ("")

    def description(self):
        descriptions = {
            "": "",
            "CORRIENTE": "CORRIENTE",
            "AHORRO": "AHORRO",
            "VISTA": "VISTA",
            "OTRO": ""
        }
        return descriptions.get(self.value, "")