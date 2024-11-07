from enum import Enum

class TipoEnvioLibroEnum(Enum):
    NotSet = (0, "")
    Total = (1, "TOTAL")
    Parcial = (2, "PARCIAL")
    Final = (3, "FINAL")
    Ajuste = (4, "AJUSTE")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
