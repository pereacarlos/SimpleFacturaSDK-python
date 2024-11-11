from enum import Enum
import json

class AmbienteEnum(Enum):
    Certificacion = 0
    Produccion = 1

    def descripcion(self):
        descripcion = {
            0: "Certificación",
            1: "Producción"
        }
