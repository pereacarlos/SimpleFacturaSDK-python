from dataclasses import dataclass, field
from typing import List, Optional
from SimpleFacturaSDK.enum.CodigosAduana import ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, Paises, TipoBulto

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Aduana:
    CodModVenta: ModalidadVenta = ModalidadVenta.NotSet
    CodClauVenta: ClausulaCompraVenta = ClausulaCompraVenta.NotSet
    CodViaTransp: ViasdeTransporte = ViasdeTransporte.NotSet
    RUTCiaTransp: str = ""
    CodPtoEmbarque: Puertos = Puertos.NotSet
    CodPtoDesemb: Puertos = Puertos.NotSet
    CodUnidMedTara: UnidadMedida = UnidadMedida.NotSet
    CodUnidPesoBruto: UnidadMedida = UnidadMedida.NotSet
    CodUnidPesoNeto: UnidadMedida = UnidadMedida.NotSet
    CodPaisRecep: Paises = Paises.NotSet
    CodPaisDestin: Paises = Paises.NotSet
    TotItems: int = 0
    TotBultos: int = 0
    TipoBultos: List[TipoBulto] = field(default_factory=list)

    __totalClausulaVenta: float = field(default=0.0, init=False)
    __nombreTransporte: str = field(default="", init=False)
    __nombreCiaTransporte: str = field(default="", init=False)
    __idAdicionalCiaTransporte: str = field(default="", init=False)
    __booking: str = field(default="", init=False)
    __codigoOperador: str = field(default="", init=False)
    __idAdicionalPtoEmbarque: str = field(default="", init=False)
    __idAdicionalPtoDesembarque: str = field(default="", init=False)
    __pesoBruto: float = field(default=0.0, init=False)
    __pesoNeto: float = field(default=0.0, init=False)
    __montoFlete: float = field(default=0.0, init=False)
    __montoSeguro: float = field(default=0.0, init=False)

    @property
    def TotClauVenta(self) -> float:
        return round(self.__totalClausulaVenta, 2)

    @TotClauVenta.setter
    def TotClauVenta(self, value: float):
        self.__totalClausulaVenta = value

    @property
    def NombreTransp(self) -> str:
        return self.__nombreTransporte

    @NombreTransp.setter
    def NombreTransp(self, value: str):
        self.__nombreTransporte = truncate(value, 40)

    @property
    def NomCiaTransp(self) -> str:
        return self.__nombreCiaTransporte

    @NomCiaTransp.setter
    def NomCiaTransp(self, value: str):
        self.__nombreCiaTransporte = truncate(value, 40)

    @property
    def IdAdicTransp(self) -> str:
        return self.__idAdicionalCiaTransporte

    @IdAdicTransp.setter
    def IdAdicTransp(self, value: str):
        self.__idAdicionalCiaTransporte = truncate(value, 20)

    @property
    def Booking(self) -> str:
        return self.__booking

    @Booking.setter
    def Booking(self, value: str):
        self.__booking = truncate(value, 20)

    @property
    def Operador(self) -> str:
        return self.__codigoOperador

    @Operador.setter
    def Operador(self, value: str):
        self.__codigoOperador = truncate(value, 20)

    @property
    def IdAdicPtoEmb(self) -> str:
        return self.__idAdicionalPtoEmbarque

    @IdAdicPtoEmb.setter
    def IdAdicPtoEmb(self, value: str):
        self.__idAdicionalPtoEmbarque = truncate(value, 20)

    @property
    def IdAdicPtoDesemb(self) -> str:
        return self.__idAdicionalPtoDesembarque

    @IdAdicPtoDesemb.setter
    def IdAdicPtoDesemb(self, value: str):
        self.__idAdicionalPtoDesembarque = truncate(value, 20)

    @property
    def PesoBruto(self) -> float:
        return round(self.__pesoBruto, 2)

    @PesoBruto.setter
    def PesoBruto(self, value: float):
        self.__pesoBruto = value

    @property
    def PesoNeto(self) -> float:
        return round(self.__pesoNeto, 2)

    @PesoNeto.setter
    def PesoNeto(self, value: float):
        self.__pesoNeto = value

    @property
    def MntFlete(self) -> float:
        return round(self.__montoFlete, 4)

    @MntFlete.setter
    def MntFlete(self, value: float):
        self.__montoFlete = value

    @property
    def MntSeguro(self) -> float:
        return round(self.__montoSeguro, 4)

    @MntSeguro.setter
    def MntSeguro(self, value: float):
        self.__montoSeguro = value


    def __init__(self):
        self.CodModVenta = ModalidadVenta.NOT_SET
        self.CodClauVenta = ClausulaCompraVenta.NOT_SET
        self.TotClauVenta = 0.0
        self.CodViaTransp = ViasdeTransporte.NOT_SET
        self.NombreTransp = ''
        self.RUTCiaTransp = ''
        self.NomCiaTransp = ''
        self.IdAdicTransp = ''
        self.Booking = ''
        self.Operador = ''
        self.CodPtoEmbarque = Puertos.NOT_SET
        self.IdAdicPtoEmb = ''
        self.CodPtoDesemb = Puertos.NOT_SET
        self.IdAdicPtoDesemb = ''
        self.Tara = 0
        self.CodUnidMedTara = UnidadMedida.NOT_SET
        self.PesoBruto = 0.0
        self.CodUnidPesoBruto = UnidadMedida.NOT_SET
        self.PesoNeto = 0.0
        self.CodUnidPesoNeto = UnidadMedida.NOT_SET
        self.TotItems = 0
        self.TotBultos = 0
        self.TipoBultos = []
        self.MntFlete = 0.0
        self.MntSeguro = 0.0
        self.CodPaisRecep = Paises.NOT_SET
        self.CodPaisDestin = Paises.NOT_SET
