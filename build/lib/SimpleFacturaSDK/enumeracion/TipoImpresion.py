from enum import Enum

class TipoImpresionEnum(Enum):
    N = "N"
    T = "T"

    def description(self):
        descriptions = {
            TipoImpresionEnum.N: "Normal",
            TipoImpresionEnum.T: "Ticket",
        }
        return descriptions.get(self, "")