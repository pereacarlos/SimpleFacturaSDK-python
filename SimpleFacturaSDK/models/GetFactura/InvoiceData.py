from pydantic import BaseModel
class InvoiceData(BaseModel):
    tipo_dte: int
    rut_emisor: str
    rut_receptor: str 
    folio: int 
    fecha_emision: str 
    total: float    


    