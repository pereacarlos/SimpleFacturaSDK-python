from enum import Enum
import json
class CodigoTrasladoEnum(Enum):
    NotSet = (0, "No Asignado")
    Exportador = (1, "Exportador")
    AgenteAduana = (2, "Agente de Aduana")
    Vendedor = (3, "Vendedor")
    ContribuyenteAutorizado = (4, "Contribuyente autorizado por el SII")

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