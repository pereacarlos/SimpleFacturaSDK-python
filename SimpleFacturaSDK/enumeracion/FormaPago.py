from enum import Enum
import json

class FormaPagoEnum(Enum):
    NotSet = (0, "No Asignado")
    Contado = (1, "Contado")
    Credito = (2, "Crédito")
    SinCosto = (3, "Sin Costo")

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
