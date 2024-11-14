from enum import Enum


class TipoLCEEnum(Enum):
    NotSet = 0
    Contable = 1
    Remuneraciones = 2
    Honorarios = 3
    RegistroExistencia = 4
    ActivoFijo = 5
    CompraVenta = 6

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
        return descriptions.get(self.value, "")
  