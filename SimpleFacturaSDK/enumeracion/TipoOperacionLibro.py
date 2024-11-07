from enum import Enum

class TipoOperacionLibroEnum(Enum):
    NotSet = (0, "")
    Venta = (1, "VENTA")
    Compra = (2, "COMPRA")

    @property
    def xml_enum(self):
        return self.value[1]
