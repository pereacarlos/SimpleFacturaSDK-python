from enum import Enum
import json

class ExpresionDineroEnum(Enum):
    NotSet = (0, "Aún no se ha definido un valor.")
    Porcentaje = (1, "El valor se expresa como porcentaje")
    Pesos = (2, "El valor se expresa en pesos.")

    @property
    def xml_enum(self):
        xml_mapping = {
            self.NotSet: "",
            self.Porcentaje: "%",
            self.Pesos: "$"
        }
        return xml_mapping[self]

    @property
    def description(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)