from enum import Enum
import json

class TipoSobreEnvio(Enum):
    AlSII = (0, "Al SII")
    AlReceptor = (1, "Al Receptor")

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value  # Asignamos el valor interno del Enum
        obj.description = description  # Asignamos la descripción
        return obj

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
