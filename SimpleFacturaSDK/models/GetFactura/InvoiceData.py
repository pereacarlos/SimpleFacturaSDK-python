from dataclasses import dataclass

@dataclass
class InvoiceData:
    tipo_dte: int
    rut_emisor: str
    rut_receptor: str 
    folio: int 
    fecha_emision: str 
    total: float    

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            tipo_dte=data.get('tipo_dte'),
            rut_emisor=data.get('rut_emisor'),
            rut_receptor=data.get('rut_receptor'),
            folio=data.get('folio'),
            fecha_emision=data.get('fecha_emision'),
            total=data.get('total')
        )