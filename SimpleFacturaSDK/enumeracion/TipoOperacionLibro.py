from enum import Enum
import json

class TipoOperacionLibroEnum(Enum):
    NotSet = (0, "")
    Venta = (1, "VENTA")
    Compra = (2, "COMPRA")

    @property
    def xml_enum(self):
        return self.value[0]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
