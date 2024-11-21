from enum import Enum

class RejectionType(Enum):
    RCD = 1
    RFP = 3
    RFT = 4

    def description(self):
        descriptions = {
            1: "Reclamo al Contenido del Documento",
            3: "Reclamo por Falta Parcial de Mercaderías",
            4: "Reclamo por Falta Total de Mercaderías"
        }
        return descriptions.get(self.value, "")