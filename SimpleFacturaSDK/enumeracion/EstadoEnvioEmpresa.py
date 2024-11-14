from enum import Enum
import json

class EstadoEnvioEmpresaEnum(Enum):
    OK = 0
    ErrorSchema = 1
    ErrorFirma = 2
    RUTReceptorNoCorresponde = 3
    ArchivoRepetido = 90
    ArchivoIlegible = 91
    RechazoOtraRazon = 99

    def description(self):
        descriptions = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            90: "90",
            91: "91",
            99: "99"
        }
        return descriptions.get(self.value, "")

    @staticmethod
    def glosa(state, motivo_rechazo=""):
        if state == EstadoEnvioEmpresaEnum.OK:
            return "Envío recibido conforme."
        elif state == EstadoEnvioEmpresaEnum.ErrorSchema:
            return "Envío rechazado - Error de Schema."
        elif state == EstadoEnvioEmpresaEnum.ErrorFirma:
            return "Envío rechazado - Error de firma."
        elif state == EstadoEnvioEmpresaEnum.RUTReceptorNoCorresponde:
            return "Envío rechazado - Rut receptor no corresponde."
        elif state == EstadoEnvioEmpresaEnum.ArchivoRepetido:
            return "Envío rechazado - Archivo repetido"
        elif state == EstadoEnvioEmpresaEnum.ArchivoIlegible:
            return "Envío rechazado - Archivo ilegible."
        elif state == EstadoEnvioEmpresaEnum.RechazoOtraRazon:
            return f"Envío rechazado - Otra razón: {motivo_rechazo}"
        else:
            raise ValueError("Invalid state.")
