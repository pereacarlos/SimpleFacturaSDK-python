from enum import Enum
import json

class TipoImpresionEnum(Enum):
    N = "Normal"
    T = "Ticket"

    @property
    def description(self):
        return self.value

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)