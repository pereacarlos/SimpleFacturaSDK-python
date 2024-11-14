from enum import Enum


class OperacionDetalleEnum(Enum):
    NotSet = 0
    Agrega = 1
    Elimina = 2

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2"
        }
        return descriptions.get(self.value, "")