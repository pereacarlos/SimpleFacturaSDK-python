from enum import Enum
import json

class ResponseType(Enum):
    NotSet = (0, "No Asignado")
    ErrorDigitacion = (1, "Error de digitación")
    ReclamoCliente = (2, "Reclamo de Cliente")
    DatosDesactualizados = (3, "Datos Desactualizados")
    InteresesMora = (4, "Intereses por Mora")
    InteresesCambioFecha = (5, "Intereses por Cambio de Fecha")
    Otros = (6, "Otros")

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