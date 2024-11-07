from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.enum.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.enum.TipoImpuesto import TipoImpuestoEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class DetalleExportacion:
    NroLinDet: int = 0
    CdgItem: Optional[List[CodigoItem]] = None
    IndExe: IndicadorFacturacionExencionEnum = IndicadorFacturacionExencionEnum.NotSet
    Retenedor: Optional[Retenedor] = None
    Subcantidad: Optional[List[SubCantidad]] = None
    FechaElaboracionString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    FechaVencimientoString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    OtrMnda: Optional[OtraMonedaDetalle] = None
    recargo_monto: int = 0
    SubDscto: Optional[List[SubDescuento]] = None
    SubRecargo: Optional[List[SubRecargo]] = None
    CodigoImpuestoAdicional: Optional[List[TipoImpuestoEnum]] = None

    __nombre: str = field(default="", init=False)
    __descripcion: str = field(default="", init=False)
    __cantidadUnidadMedidaReferencia: float = field(default=0.0, init=False)
    __unidadMedidaReferencia: str = field(default="", init=False)
    __precioUnitarioUnidadMedidaReferencia: float = field(default=0.0, init=False)
    __cantidad: float = field(default=0.0, init=False)
    __unidadMedida: str = field(default="", init=False)
    __precio: float = field(default=0.0, init=False)
    __descuentoPorcentaje: float = field(default=0.0, init=False)
    __recargoPorcentaje: float = field(default=0.0, init=False)
    __montoItem: float = field(default=0.0, init=False)

    @property
    def NmbItem(self) -> str:
        return self.__nombre

    @NmbItem.setter
    def NmbItem(self, value: str):
        self.__nombre = truncate(value, 80)

    @property
    def DscItem(self) -> str:
        return self.__descripcion

    @DscItem.setter
    def DscItem(self, value: str):
        self.__descripcion = truncate(value, 1000)

    @property
    def QtyRef(self) -> float:
        return round(self.__cantidadUnidadMedidaReferencia, 6)

    @QtyRef.setter
    def QtyRef(self, value: float):
        self.__cantidadUnidadMedidaReferencia = value

    @property
    def UnmdRef(self) -> str:
        return self.__unidadMedidaReferencia

    @UnmdRef.setter
    def UnmdRef(self, value: str):
        self.__unidadMedidaReferencia = truncate(value, 4)

    @property
    def PrcRef(self) -> float:
        return round(self.__precioUnitarioUnidadMedidaReferencia, 6)

    @PrcRef.setter
    def PrcRef(self, value: float):
        self.__precioUnitarioUnidadMedidaReferencia = value

    @property
    def QtyItem(self) -> float:
        return round(self.__cantidad, 6)

    @QtyItem.setter
    def QtyItem(self, value: float):
        self.__cantidad = value

    @property
    def FchElabor(self) -> datetime:
        return datetime.strptime(self.FechaElaboracionString, "%Y-%m-%d")

    @FchElabor.setter
    def FchElabor(self, value: datetime):
        self.FechaElaboracionString = value.strftime("%Y-%m-%d")

    @property
    def FchVencim(self) -> datetime:
        return datetime.strptime(self.FechaVencimientoString, "%Y-%m-%d")

    @FchVencim.setter
    def FchVencim(self, value: datetime):
        self.FechaVencimientoString = value.strftime("%Y-%m-%d")

    @property
    def UnmdItem(self) -> str:
        return self.__unidadMedida

    @UnmdItem.setter
    def UnmdItem(self, value: str):
        self.__unidadMedida = truncate(value, 4)

    @property
    def PrcItem(self) -> float:
        return self.__precio

    @PrcItem.setter
    def PrcItem(self, value: float):
        self.__precio = value

    @property
    def DescuentoPct(self) -> float:
        return round(self.__descuentoPorcentaje, 2)

    @DescuentoPct.setter
    def DescuentoPct(self, value: float):
        self.__descuentoPorcentaje = value

    @property
    def RecargoPct(self) -> float:
        return round(self.__recargoPorcentaje, 2)

    @RecargoPct.setter
    def RecargoPct(self, value: float):
        self.__recargoPorcentaje = value

    @property
    def MontoItem(self) -> float:
        return round(self.__montoItem, 6)

    @MontoItem.setter
    def MontoItem(self, value: float):
        self.__montoItem = value


    def __init__(self):
        self.NroLinDet = 0
        self.NmbItem = ''
        self.MontoItem = 0.0
        self.CdgItem = []
        self.IndExe = IndicadorFacturacionExencionEnum.NotSet
        self.Retenedor = None
        self.DscItem = ''
        self.QtyRef = 0.0
        self.UnmdRef = ''
        self.PrcRef = 0.0
        self.QtyItem = 0.0
        self.Subcantidad = []
        self.FchElabor = datetime.min
        self.FchVencim = datetime.min
        self.UnmdItem = ''
        self.PrcItem = 0.0
        self.OtrMnda = None
        self.DescuentoPct = 0.0
        self.DescuentoMonto = 0
        self.SubDscto = []
        self.RecargoPct = 0.0
        self.RecargoMonto = 0
        self.SubRecargo = []
        self.CodigoImpuestoAdicional = []
