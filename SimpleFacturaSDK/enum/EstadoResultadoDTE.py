from enum import Enum

class EstadoResultadoDTEEnum(Enum):
    Ok = (0, "DTE Aceptado OK.")
    AceptadoReparos = (1, "DTE Aceptado con Discrepancia.")
    Rechazo = (2, "DTE Rechazado.")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class EstadoResultadoDTE:
    Motivo = ""

    @staticmethod
    def glosa(state):
        if state == EstadoResultadoDTEEnum.Ok:
            return f"DTE Aceptado OK. {EstadoResultadoDTE.Motivo}"
        elif state == EstadoResultadoDTEEnum.AceptadoReparos:
            return f"DTE Aceptado con discrepancias - {EstadoResultadoDTE.Motivo}"
        elif state == EstadoResultadoDTEEnum.Rechazo:
            return f"DTE Rechazado - {EstadoResultadoDTE.Motivo}"
        else:
            raise ValueError("Invalid state")
