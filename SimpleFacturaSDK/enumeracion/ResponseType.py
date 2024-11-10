from enum import Enum
import json

class ResponseType(Enum):
    Accepted = (3, "Aceptado")
    AcceptedWithQualms = (4, "Contado")
    Rejected = (5, "Crédito")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  
        return super().default(obj)