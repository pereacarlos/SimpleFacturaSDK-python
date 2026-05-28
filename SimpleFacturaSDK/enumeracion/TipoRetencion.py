from enum import Enum

class TipoRetencion(Enum):
    Receptor = 1
    Contribuyente = 2

    def descripcion(self):
        descripcion = {
            1: "Receptor",
            2: "Contribuyente"
        }

        return descripcion.get(self.value, "Tipo de retención no definido")
