from enum import Enum
import json

class TipoSalidaEnum(Enum):
    Base64 = (0, "Base64")
    XML = (1, "XML")

    @property
    def xml_enum(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)