from enum import Enum

class EstadoEnvioEmpresaEnum(Enum):
    OK = (0, "Envío recibido conforme.")
    ErrorSchema = (1, "Envío rechazado - Error de Schema.")
    ErrorFirma = (2, "Envío rechazado - Error de firma.")
    RUTReceptorNoCorresponde = (3, "Envío rechazado - Rut receptor no corresponde.")
    ArchivoRepetido = (90, "Envío rechazado - Archivo repetido")
    ArchivoIlegible = (91, "Envío rechazado - Archivo ilegible.")
    RechazoOtraRazon = (99, "Envío rechazado - Otra razón.")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

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

