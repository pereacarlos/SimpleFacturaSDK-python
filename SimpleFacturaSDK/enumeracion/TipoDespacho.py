from enum import Enum
import json

class TipoDespachoEnum(Enum):
    NotSet = (0, "No Asignado")
    Receptor = (1, "Receptor")
    EmisorACliente = (2, "Emisor A Cliente")
    EmisorAOtrasInstalaciones = (3, "Emisor A Otras Instalaciones")

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