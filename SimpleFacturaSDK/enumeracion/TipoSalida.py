from enum import Enum
import json

class TipoSalidaEnum(Enum):
    Base64 = 0
    XML = 1

    def description(self):
        descriptions = {
            0: "Base64",
            1: "XML"
        }