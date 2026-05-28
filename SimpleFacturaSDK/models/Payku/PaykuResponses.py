from dataclasses import dataclass


@dataclass
class PaykuTransaccionResponse:
    fecha: str = ""
    monto: float = 0
    estado: str = ""
    receptorRut: str = ""
    receptorRazonSocial: str = ""
    porcentaje: float = 0
    montoNeto: float = 0
    dteFolio: int = 0
    tipo: str = ""
