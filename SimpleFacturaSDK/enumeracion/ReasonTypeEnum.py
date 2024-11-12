from enum import Enum
import json

class ReasonTypeEnum(Enum):
    NotSet = 0
    ErrorDigitacion = 1
    ReclamoCliente = 2
    DatosDesactualizados = 3
    InteresesMora = 4
    InteresesCambioFecha = 5
    Otros = 6

    def  description(self):
        descriptions = {
            0: "No Asignado",
            1: "Error de Digitación",
            2: "Reclamo del Cliente",
            3: "Datos Desactualizados",
            4: "Intereses por Mora",
            5: "Intereses por Cambio de Fecha",
            6: "Otros"
        }
        return descriptions(self.value, "")