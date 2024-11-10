from enum import Enum
import json

class AmbienteEnum(Enum):
    Certificacion = (0, "Certificación")
    Produccion = (1, "Producción")

    @property
    def code(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)