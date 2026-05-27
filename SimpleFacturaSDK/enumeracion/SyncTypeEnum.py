from enum import Enum
import json

class SyncTypeEnum(Enum):
    Ventas = 1
    Compras = 2
    BheEmitidas = 3
    BheRecibidas = 4

    def description(self):
        descriptions = {
            1: "Ventas",
            2: "Compras",
            3: "Bhe Emitidas",
            4: "Bhe Recibidas"
        }
        return descriptions.get(self.value, "")