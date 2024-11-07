from enum import Enum

class EstadoRecepcionDTEEnum(Enum):
    Ok = (0, "DTE Recibido OK.")
    ErrorFirma = (1, "DTE No Recibido - Error de firma.")
    ErrorRutEmisor = (2, "DTE No Recibido - Error en RUT Emisor.")
    ErrorRutReceptor = (3, "DTE No Recibido - Error en RUT Receptor.")
    Repetido = (4, "DTE No Recibido - DTE Repetido.")
    Otra = (99, "DTE No Recibido - Otra.")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

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
