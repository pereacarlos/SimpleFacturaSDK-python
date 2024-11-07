from enum import Enum

class TipoLCEEnum(Enum):
    NotSet = (0, "")
    Contable = (1, "1")
    Remuneraciones = (2, "2")
    Honorarios = (3, "3")
    RegistroExistencia = (4, "4")
    ActivoFijo = (5, "5")
    CompraVenta = (6, "6")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
