from enum import Enum
import json

class FormaPagoEnum(Enum):
    NotSet = 0
    Contado = 1
    Credito = 2
    SinCosto = 3

    def description(self):
        descriptions = {
            0:"",
            1:"1",
            2:"2",
            3:"3"
        }
        return descriptions(self.value, "")