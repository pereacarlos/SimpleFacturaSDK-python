from enum import Enum
import json

class TipoDespachoEnum(Enum):
    NotSet = 0
    Receptor = 1
    EmisorACliente = 2
    EmisorAOtrasInstalaciones = 3

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3"
        }
        return descriptions.get(self.value, "")