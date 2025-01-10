from dataclasses import dataclass, field

@dataclass

class CesionDteRequest:
    CorreoDeudor: str
    RutCesionario: str
    RutPersonaAutorizada: str
    OtrasCondiciones: str
    Folio: int
    RutEmpresa: str