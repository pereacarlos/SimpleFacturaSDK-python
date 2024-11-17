from enum import Enum

class EstadoResultadoDTEEnum(Enum):
    Ok = 0
    AceptadoReparos = 1
    Rechazo = 2

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2"
        }
        return descriptions(self.value,"")
Motivo = ""

@staticmethod
def glosa(state):
    if state == EstadoResultadoDTEEnum.Ok:
        return f"DTE Aceptado OK. {Motivo}"
    elif state == EstadoResultadoDTEEnum.AceptadoReparos:
        return f"DTE Aceptado con discrepancias - {Motivo}"
    elif state == EstadoResultadoDTEEnum.Rechazo:
        return f"DTE Rechazado - {Motivo}"
    else:
        raise ValueError("Invalid state")
