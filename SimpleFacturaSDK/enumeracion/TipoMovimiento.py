from enum import Enum
import json

class TipoMovimientoEnum(Enum):
    NotSet = (0, "Aún no se ha definido un valor.")
    Descuento = (1, "Descuento")
    Recargo = (2, "Recargo")

    @property
    def xml_enum(self):
        xml_mapping = {
            self.NotSet: "",
            self.Descuento: "D",
            self.Recargo: "R"
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