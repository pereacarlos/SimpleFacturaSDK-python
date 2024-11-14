from enum import Enum
import json

class TipoAceptacion(Enum):
    ACD = 0
    RCD = 1
    ERM = 2
    RFP = 3
    RFT = 4

    def description(self):
        descriptions = {
            0: "Aceptación de Contenido del Documento",
            1: "Reclamo al Contenido del Documento",
            2: "Otorga Recibo de Mercaderías o Servicios",
            3: "Reclamo por Falta Parcial de Mercaderías",
            4: "Reclamo por Falta Total de Mercaderías"
        }
        return descriptions.get(self.value, "")