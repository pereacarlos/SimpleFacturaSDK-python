from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, Paises
from SimpleFacturaSDK.models.GetFactura.TipoBulto import TipoBulto

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Aduana:
    CodModVenta: ModalidadVenta
    CodClauVenta: ClausulaCompraVenta
    TotClauVenta: float
    CodViaTransp: ViasdeTransporte
    NombreTransp: str
    RUTCiaTransp: str
    NomCiaTransp: str
    IdAdicTransp: str
    Booking: str
    Operador: str
    CodPtoEmbarque: Puertos
    IdAdicPtoEmb: str
    PesoBruto: float
    CodUnidPesoBruto: UnidadMedida
    PesoNeto: float
    CodUnidPesoNeto: UnidadMedida
    TotItems: int
    TotBultos: int
    CodPtoDesemb: Puertos
    CodPaisDestin: Paises
    CodPaisRecep: Paises
    CodPaisTransito: Paises
    TipoBultos: List[TipoBulto] = field(default_factory=list)

    def __post_init__(self):
        self.NombreTransp = truncate(self.NombreTransp, 70)
        self.RUTCiaTransp = truncate(self.RUTCiaTransp, 10)
        self.NomCiaTransp = truncate(self.NomCiaTransp, 70)
        self.IdAdicTransp = truncate(self.IdAdicTransp, 20)
        self.Booking = truncate(self.Booking, 15)
        self.Operador = truncate(self.Operador, 15)
        self.IdAdicPtoEmb = truncate(self.IdAdicPtoEmb, 20)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            CodModVenta=ModalidadVenta(data.get('CodModVenta')),
            CodClauVenta=ClausulaCompraVenta(data.get('CodClauVenta')),
            TotClauVenta=data.get('TotClauVenta'),
            CodViaTransp=ViasdeTransporte(data.get('CodViaTransp')),
            NombreTransp=data.get('NombreTransp'),
            RUTCiaTransp=data.get('RUTCiaTransp'),
            NomCiaTransp=data.get('NomCiaTransp'),
            IdAdicTransp=data.get('IdAdicTransp'),
            Booking=data.get('Booking'),
            Operador=data.get('Operador'),
            CodPtoEmbarque=Puertos(data.get('CodPtoEmbarque')),
            IdAdicPtoEmb=data.get('IdAdicPtoEmb'),
            PesoBruto=data.get('PesoBruto'),
            CodUnidPesoBruto=UnidadMedida(data.get('CodUnidPesoBruto')),
            PesoNeto=data.get('PesoNeto'),
            CodUnidPesoNeto=UnidadMedida(data.get('CodUnidPesoNeto')),
            TotItems=data.get('TotItems'),
            TotBultos=data.get('TotBultos'),
            CodPtoDesemb=Puertos(data.get('CodPtoDesemb')),
            CodPaisDestin=Paises(data.get('CodPaisDestin')),
            CodPaisRecep=Paises(data.get('CodPaisRecep')),
            CodPaisTransito=Paises(data.get('CodPaisTransito')),
            TipoBultos=[TipoBulto.from_dict(tb) for tb in data.get('TipoBultos', [])]
        )

    def to_dict(self):
        return {
            'CodModVenta': self.CodModVenta.value,
            'CodClauVenta': self.CodClauVenta.value,
            'TotClauVenta': self.TotClauVenta,
            'CodViaTransp': self.CodViaTransp.value,
            'NombreTransp': self.NombreTransp,
            'RUTCiaTransp': self.RUTCiaTransp,
            'NomCiaTransp': self.NomCiaTransp,
            'IdAdicTransp': self.IdAdicTransp,
            'Booking': self.Booking,
            'Operador': self.Operador,
            'CodPtoEmbarque': self.CodPtoEmbarque.value,
            'IdAdicPtoEmb': self.IdAdicPtoEmb,
            'PesoBruto': self.PesoBruto,
            'CodUnidPesoBruto': self.CodUnidPesoBruto.value,
            'PesoNeto': self.PesoNeto,
            'CodUnidPesoNeto': self.CodUnidPesoNeto.value,
            'TotItems': self.TotItems,
            'TotBultos': self.TotBultos,
            'CodPtoDesemb': self.CodPtoDesemb.value,
            'CodPaisDestin': self.CodPaisDestin.value,
            'CodPaisRecep': self.CodPaisRecep.value,
            'CodPaisTransito': self.CodPaisTransito.value,
            'TipoBultos': [tb.to_dict() for tb in self.TipoBultos]
        }