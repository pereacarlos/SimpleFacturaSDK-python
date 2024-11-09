from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.enumeracion.CodigosAduana import ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, Paises, TipoBulto

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Aduana:
    CodModVenta: ModalidadVenta = ModalidadVenta.NotSet
    CodClauVenta: ClausulaCompraVenta = ClausulaCompraVenta.NotSet
    TotClauVenta: float = 0.0
    CodViaTransp: ViasdeTransporte = ViasdeTransporte.NotSet
    NombreTransp: str = ""
    RUTCiaTransp: str = ""
    NomCiaTransp: str = ""
    IdAdicTransp: str = ""
    Booking: str = ""
    Operador: str = ""
    CodPtoEmbarque: Puertos = Puertos.NotSet
    IdAdicPtoEmb: str = ""
    CodPtoDesemb: Puertos = Puertos.NotSet
    IdAdicPtoDesemb: str = ""
    Tara: int = 0
    CodUnidMedTara: UnidadMedida = UnidadMedida.NotSet
    PesoBruto: float = 0.0
    CodUnidPesoBruto: UnidadMedida = UnidadMedida.NotSet
    PesoNeto: float = 0.0
    CodUnidPesoNeto: UnidadMedida = UnidadMedida.NotSet
    TotItems: int = 0
    TotBultos: int = 0
    TipoBultos: List[TipoBulto] = field(default_factory=list)
    MntFlete: float = 0.0
    MntSeguro: float = 0.0
    CodPaisRecep: Paises = Paises.NotSet
    CodPaisDestin: Paises = Paises.NotSet
   
    __totalClausulaVenta: float = field(default=0.0, metadata={"decimals": 2})
    __nombreTransporte: str = field(default="", metadata={"max_length": 40})
    __nombreCiaTransporte: str = field(default="", metadata={"max_length": 40})
    __idAdicionalCiaTransporte: str = field(default="", init=False)
    __booking: str = field(default="", metadata={"max_length": 20})
    __codigoOperador: str = field(default="", metadata={"max_length": 20})
    __idAdicionalPtoEmbarque: str = field(default="", metadata={"max_length": 20})
    __idAdicionalPtoDesembarque: str = field(default="", init=False)
    __pesoBruto: float = field(default=0.0, metadata={"decimals": 2})
    __pesoNeto: float = field(default=0.0, metadata={"decimals": 2})
    __montoFlete: float = field(default=0.0, metadata={"decimals": 4})
    __montoSeguro: float = field(default=0.0, metadata={"decimals": 4})

    def __post_init__(self):
        self.__totalClausulaVenta = round(self.TotClauVenta, 2)
        self.__nombreTransporte = truncate(self.NombreTransp, 40)
        self.__nombreCiaTransporte = truncate(self.NomCiaTransp, 40)
        self.__idAdicionalCiaTransporte = truncate(self.IdAdicTransp, 20)
        self.__booking = truncate(self.Booking, 20)
        self.__codigoOperador = truncate(self.Operador, 20)
        self.__idAdicionalPtoEmbarque = truncate(self.IdAdicPtoEmb, 20)
        self.__idAdicionalPtoDesembarque = self.IdAdicPtoDesemb
        self.__pesoBruto = round(self.PesoBruto, 2)
        self.__pesoNeto =  round(self.PesoNeto, 2)
        self.__montoFlete = round(self.MntFlete, 4)
        self.__montoSeguro = round(self.MntSeguro, 4)

  

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            CodModVenta=data.get('CodModVenta'),
            CodClauVenta=data.get('CodClauVenta'),
            TotClauVenta=data.get('TotClauVenta'),
            CodViaTransp=data.get('CodViaTransp'),
            NombreTransp=data.get('NombreTransp'),
            RUTCiaTransp=data.get('RUTCiaTransp'),
            NomCiaTransp=data.get('NomCiaTransp'),
            IdAdicTransp=data.get('IdAdicTransp'),
            Booking=data.get('Booking'),
            Operador=data.get('Operador'),
            CodPtoEmbarque=data.get('CodPtoEmbarque'),
            IdAdicPtoEmb=data.get('IdAdicPtoEmb'),
            CodPtoDesemb=data.get('CodPtoDesemb'),
            IdAdicPtoDesemb=data.get('IdAdicPtoDesemb'),
            Tara=data.get('Tara'),
            CodUnidMedTara=data.get('CodUnidMedTara'),
            PesoBruto=data.get('PesoBruto'),
            CodUnidPesoBruto=data.get('CodUnidPesoBruto'),
            PesoNeto=data.get('PesoNeto'),
            CodUnidPesoNeto=data.get('CodUnidPesoNeto'),
            TotItems=data.get('TotItems'),
            TotBultos=data.get('TotBultos'),
            TipoBultos=data.get('TipoBultos'),
            MntFlete=data.get('MntFlete'),
            MntSeguro=data.get('MntSeguro'),
            CodPaisRecep=data.get('CodPaisRecep'),
            CodPaisDestin=data.get('CodPaisDestin')
        )