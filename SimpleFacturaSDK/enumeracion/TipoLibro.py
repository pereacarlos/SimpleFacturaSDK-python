from enum import Enum
import json

class TipoLibroEnum(Enum):
    NotSet = (0, "")
    Mensual = (1, "MENSUAL")
    Especial = (2, "ESPECIAL")
    Rectifica = (3, "RECTIFICA")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class TipoLibroOrigenEnum(Enum):
    NotSet = (0, "")
    IECV = (1, "IECV")
    Boletas = (2, "BOLETAS")
    Guias = (3, "GUIAS")

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
