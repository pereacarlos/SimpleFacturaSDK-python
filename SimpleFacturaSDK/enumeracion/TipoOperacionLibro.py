from enum import Enum


class TipoOperacionLibroEnum(Enum):
    NotSet = 0
    Venta = 1
    Compra = 2

    def description(self):
        descriptions = {
            0: "",
            1: "VENTA",
            2: "COMPRA"
        }
        return descriptions.get(self.value, "")