from enum import Enum

class OperacionDetalleEnum(Enum):
    NotSet = (0, "")
    Agrega = (1, "Agrega")
    Elimina = (2, "Elimina")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
