from enum import Enum
import json

class TipoCertificadoEnum(Enum):
    NotSet = ("")
    Certificacion = ("Certificación")
    Produccion = ("Producción")
    @property
    def xml_enum(self):
        return self.value[0]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
