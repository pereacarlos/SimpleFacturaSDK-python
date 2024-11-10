from enum import Enum
import json

class TipoServicioEnum(Enum):
    NotSet = (0, "")
    BoletaServiciosPeriodicos = (1, "1")
    BoletaServiciosPeriodicosDomiciliarios = (2, "2")
    BoletaVentasYServicios = (3, "3")
    BoletaEspectaculosPorTerceros = (4, "4")

    @property
    def xml_enum(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
