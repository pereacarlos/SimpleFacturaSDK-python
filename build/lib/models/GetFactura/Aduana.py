from dataclasses import dataclass, field
from typing import List, Optional
from enumeracion.CodigosAduana import ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, Paises
from models.GetFactura.TipoBulto import TipoBulto

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
    ombreTransp: Optional[str] = None
    UTCiaTransp: Optional[str] = None
    omCiaTransp: Optional[str] = None
    dAdicTransp: Optional[str] = None
    ooking: Optional[str] = None
    perador: Optional[str] = None
    CodPaisTransito: Optional[Paises] = None