from pydantic import BaseModel
class InvoiceData(BaseModel):
    tipoDTE: int
    rutEmisor: str
    rutReceptor: str
    folio: int
    fechaEmision: str
    total: float


    