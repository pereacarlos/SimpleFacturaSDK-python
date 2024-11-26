from enum import Enum
import json

class IndicadorFacturacionExencionEnum(Enum):
    NotSet = 0
    NoAfectoOExento = 1
    ProductoOServicioNoFacturable = 2
    GarantiaDeposito =3
    ItemNoVenta = 4
    ItemARebajar = 5
    ProductoOServicioNoFacturableNegativo = 6

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6"
        }
        return descriptions(self.value, "")
