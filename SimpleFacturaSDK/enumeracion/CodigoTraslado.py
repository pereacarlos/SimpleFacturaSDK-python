from enum import Enum

class CodigoTrasladoEnum(Enum):
    NotSet = 0
    Exportador = 1
    AgenteAduana = 2
    Vendedor = 3
    ContribuyenteAutorizado = 4

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4"
        }
        return descriptions(self.value, "")

   