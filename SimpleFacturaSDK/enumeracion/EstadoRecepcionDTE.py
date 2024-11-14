from enum import Enum
import json

class EstadoRecepcionDTEEnum(Enum):
    Ok = 0
    ErrorFirma = 1
    ErrorRutEmisor = 2
    ErrorRutReceptor = 3
    Repetido = 4
    Otra = 99

    def description(self):
        descriptions = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            99: "99"
        }
        return descriptions.get(self.value, "")

    @staticmethod
    def glosa(state):
        if state == EstadoRecepcionDTEEnum.Ok:
            return "DTE Recibido OK."
        elif state == EstadoRecepcionDTEEnum.ErrorFirma:
            return "DTE No Recibido - Error de firma."
        elif state == EstadoRecepcionDTEEnum.ErrorRutEmisor:
            return "DTE No Recibido - Error en RUT Emisor."
        elif state == EstadoRecepcionDTEEnum.ErrorRutReceptor:
            return "DTE No Recibido - Error en RUT Receptor."
        elif state == EstadoRecepcionDTEEnum.Repetido:
            return "DTE No Recibido - DTE Repetido."
        elif state == EstadoRecepcionDTEEnum.Otra:
            return "DTE No Recibido - Otra."
        else:
            raise ValueError("Invalid state.")
