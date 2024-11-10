from enum import Enum
import json


class TipoReferenciaEnum(Enum):
    NotSet = (0, "No Asignado", "")
    AnulaDocumentoReferencia = (1, "Anula Documento de Referencia", "1")
    CorrigeTextoDocumentoReferencia = (2, "Corrige Texto de Documento de Referencia", "2")
    CorrigeMontos = (3, "Corrige Montos de Documento de Referencia", "3")
    SetPruebas = (4, "Set de Pruebas", "SET")

    @property
    def code(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

    @property
    def xml_enum(self):
        return self.value[2]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)