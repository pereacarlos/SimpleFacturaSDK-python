from enum import Enum
import json

class OperacionDetalleEnum(Enum):
    NotSet = (0, "")
    Agrega = (1, "Agrega")
    Elimina = (2, "Elimina")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)