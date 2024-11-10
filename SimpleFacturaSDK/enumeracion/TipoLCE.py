from enum import Enum
import json

class TipoLCEEnum(Enum):
    NotSet = (0, "")
    Contable = (1, "1")
    Remuneraciones = (2, "2")
    Honorarios = (3, "3")
    RegistroExistencia = (4, "4")
    ActivoFijo = (5, "5")
    CompraVenta = (6, "6")

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
