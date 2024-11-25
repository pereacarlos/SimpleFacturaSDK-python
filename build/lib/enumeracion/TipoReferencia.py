from enum import Enum
import json


class TipoReferenciaEnum(Enum):
    NotSet = 0
    AnulaDocumentoReferencia = 1
    CorrigeTextoDocumentoReferencia = 2
    CorrigeMontos = 3
    SetPruebas = 4

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "SET"
        }
        return descriptions.get(self.value, "")

class TipoReferenciaEnum_test(Enum):
    NotSet = '0'
    AnulaDocumentoReferencia = 1
    CorrigeTextoDocumentoReferencia = 2
    CorrigeMontos = 3

    def description(self):
        descriptions = {
            '0': "SET",
            1: "1",
            2: "2",
            3: "3"
        }
        return descriptions.get(self.value, "")