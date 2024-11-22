from dataclasses import dataclass, field
from typing import List, Optional
from enumeracion.CodigosAduana import ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, Paises
from models.GetFactura.TipoBulto import TipoBulto

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Aduana:
    CodModVenta: ModalidadVenta
    CodClauVenta: ClausulaCompraVenta
    TotClauVenta: float
    CodViaTransp: ViasdeTransporte
    Tara: int
    CodUnidMedTara: UnidadMedida
    MntSeguro: float
    MntFlete: float
    CodPtoEmbarque: Puertos
    PesoBruto: float
    CodUnidPesoBruto: UnidadMedida
    PesoNeto: float
    CodUnidPesoNeto: UnidadMedida
    TotBultos: int
    CodPtoDesemb: Puertos
    CodPaisDestin: Paises
    CodPaisRecep: Paises
    TipoBultos: List[TipoBulto] 
    IdAdicPtoEmb: Optional[str] = None
    TotItems: Optional[int] = None
    NombreTransp: Optional[str] = None
    RUTCiaTransp: Optional[str] = None
    NomCiaTransp: Optional[str] = None
    IdAdicTransp: Optional[str] = None
    Booking: Optional[str] = None
    Operador: Optional[str] = None