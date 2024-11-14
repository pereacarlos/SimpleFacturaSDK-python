from enum import Enum
import json

class TipoCertificadoEnum(Enum):
    NotSet = ("")
    Certificacion = ("C")
    Produccion = ("P")
   
    def description(self):
        descriptions = {
            "": "",
            "C": "C",
            "P": "P"
        }
        return descriptions.get(self.value, "")