from enum import Enum
import json
class IndicadorAnuladoEnum(Enum):
    NotSet = 0
    Anulado = 1
    AnuladoPrevio = 1
    AnuladoPosterior = 2
    RecibidoParcialmente = 3

    def description(self):
        descriptions = {
            0: "",
            1: "A",
            1: "1",
            2: "2",
            3: "3"
        }
        return descriptions.get(self.value, "")