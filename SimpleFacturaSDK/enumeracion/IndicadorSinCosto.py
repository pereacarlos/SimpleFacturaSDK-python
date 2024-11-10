from enum import Enum
import json

class IndicadorSinCostoEnum(Enum):
    NotSet = (0, "")
    VentaSinCosto = (1, "Entrega gratuita")

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