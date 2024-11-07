from dataclasses import dataclass

@dataclass
class InvoiceData:
    tipo_dte: int
    rut_emisor: str
    rut_receptor: str 
    folio: int 
    fecha_emision: str 
    total: float    

    def __init__(self, tipo_dte: int, rut_emisor: str, rut_receptor: str, folio: int, fecha_emision: str, total: float):
        self.tipo_dte = tipo_dte
        self.rut_emisor = rut_emisor
        self.rut_receptor = rut_receptor
        self.folio = folio
        self.fecha_emision = fecha_emision
        self.total = total
