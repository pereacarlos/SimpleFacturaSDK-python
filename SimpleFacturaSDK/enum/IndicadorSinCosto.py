from enum import Enum

class IndicadorSinCostoEnum(Enum):
    NotSet = (0, "")
    VentaSinCosto = (1, "Entrega gratuita")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
