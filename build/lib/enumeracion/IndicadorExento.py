from enum import Enum
import json

class IndicadorExentoEnum(Enum):
    NotSet = 0
    Exento = 1
    NoFacturable = 2

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2"
        }
        return descriptions.get(self.value, "")

