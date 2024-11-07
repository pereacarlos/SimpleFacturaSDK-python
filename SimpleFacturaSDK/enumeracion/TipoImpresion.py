from enum import Enum

class TipoImpresionEnum(Enum):
    N = "Normal"
    T = "Ticket"

    @property
    def description(self):
        return self.value
