from enum import Enum
import json

class TipoAceptacion(Enum):
    ACD = (0, "Acepta Contenido del Documento")
    RCD = (1, "Reclamo al Contenido del Documento")
    ERM = (2, "Otorga Recibo de Mercaderías o Servicios")
    RFP = (3, "Reclamo por Falta Parcial de Mercaderías")
    RFT = (4, "Reclamo por Falta Total de Mercaderías")

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
