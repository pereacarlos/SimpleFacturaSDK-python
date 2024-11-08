from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.enumeracion.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CodigoItem
from SimpleFacturaSDK.models.GetFactura.OtraMonedaDetalle import OtraMonedaDetalle
from SimpleFacturaSDK.models.GetFactura.Retenedor import Retenedor
from SimpleFacturaSDK.models.GetFactura.SubCantidad import SubCantidad
from SimpleFacturaSDK.models.GetFactura.SubDescuento import SubDescuento
from SimpleFacturaSDK.models.GetFactura.SubRecargo import SubRecargo


def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class Detalle:
    NroLinDet: int = 0
    CdgItem: Optional[List[CodigoItem]] = None
    IndExe: IndicadorFacturacionExencionEnum = IndicadorFacturacionExencionEnum.NotSet
    Retenedor: Optional[Retenedor] = None
    NmbItem: str = field(default_factory=str)
    DscItem: str = field(default_factory=str)
    QtyRef: float = 0.0
    UnmdRef: str = field(default_factory=str)
    PrcRef: float = 0.0
    QtyItem: float = 0.0
    Subcantidad: Optional[List[SubCantidad]] = None
    FechaElaboracionString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    FechaVencimientoString: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    UnmdItem: str = field(default_factory=str)
    PrcItem: float = 0.0
    OtrMnda: Optional[OtraMonedaDetalle] = None
    DescuentoPct: float = 0.0
    recargo_monto: int = 0
    SubDscto: Optional[List[SubDescuento]] = None
    RecargoPct: float = 0.0
    SubRecargo: Optional[List[SubRecargo]] = None
    CodigoImpuestoAdicional: Optional[List[TipoImpuestoEnum]] = None
    MontoItem: int = 0

    # Private fields for internal use
    _nombre: str = field(init=False, default="")
    _descripcion: str = field(init=False, default="")
    _cantidadUnidadMedidaReferencia: float = field(init=False, default=0.0)
    _unidadMedidaReferencia: str = field(init=False, default="")
    _precioUnitarioUnidadMedidaReferencia: float = field(init=False, default=0.0)
    _cantidad: float = field(init=False, default=0.0)
    _unidadMedida: str = field(init=False, default="")
    _precio: float = field(init=False, default=0.0)
    _descuentoPorcentaje: float = field(init=False, default=0.0)
    _recargoPorcentaje: float = field(init=False, default=0.0)

    def __post_init__(self):
        self._nombre = self.NmbItem
        self._descripcion = self.DscItem
        self._cantidadUnidadMedidaReferencia = self.QtyRef
        self._unidadMedidaReferencia = self.UnmdRef
        self._precioUnitarioUnidadMedidaReferencia = self.PrcRef
        self._cantidad = self.QtyItem
        self._unidadMedida = self.UnmdItem
        self._precio = self.PrcItem
        self._descuentoPorcentaje = self.DescuentoPct
        self._recargoPorcentaje = self.RecargoPct

    @property
    def FechaElaboracion(self) -> datetime:
        return datetime.strptime(self.FechaElaboracionString, "%Y-%m-%d")

    @FechaElaboracion.setter
    def FechaElaboracion(self, value: datetime):
        self.FechaElaboracionString = value.strftime("%Y-%m-%d")

    @property
    def FechaVencimiento(self) -> datetime:
        return datetime.strptime(self.FechaVencimientoString, "%Y-%m-%d")

    @FechaVencimiento.setter
    def FechaVencimiento(self, value: datetime):
        self.FechaVencimientoString = value.strftime("%Y-%m-%d")

    @property
    def Nombre(self) -> str:
        return self._nombre

    @Nombre.setter
    def Nombre(self, value: str):
        self._nombre = truncate(value, 80)

    @property
    def Descripcion(self) -> str:
        return self._descripcion

    @Descripcion.setter
    def Descripcion(self, value: str):
        self._descripcion = truncate(value, 1000)

    @property
    def CantidadUnidadMedidaReferencia(self) -> float:
        return self._cantidadUnidadMedidaReferencia

    @CantidadUnidadMedidaReferencia.setter
    def CantidadUnidadMedidaReferencia(self, value: 6):
        self._cantidadUnidadMedidaReferencia = value

    @property
    def UnidadMedidaReferencia(self) -> str:
        return self._unidadMedidaReferencia

    @UnidadMedidaReferencia.setter
    def UnidadMedidaReferencia(self, value: str):
        self._unidadMedidaReferencia = truncate(value, 4)

    @property
    def PrecioUnitarioUnidadMedidaReferencia(self) -> float:
        return self._precioUnitarioUnidadMedidaReferencia

    @PrecioUnitarioUnidadMedidaReferencia.setter
    def PrecioUnitarioUnidadMedidaReferencia(self, value: 6):
        self._precioUnitarioUnidadMedidaReferencia = value

    @property
    def Cantidad(self) -> float:
        return self._cantidad

    @Cantidad.setter
    def Cantidad(self, value: 6):
        self._cantidad = value

    @property
    def UnidadMedida(self) -> str:
        return self._unidadMedida

    @UnidadMedida.setter
    def UnidadMedida(self, value: str):
        self._unidadMedida = truncate(value, 4)

    @property
    def Precio(self) -> float:
        return self._precio

    @Precio.setter
    def Precio(self, value: float):
        self._precio = value


    @property
    def DescuentoPorcentaje(self) -> float:
        return self._descuentoPorcentaje

    @DescuentoPorcentaje.setter
    def DescuentoPorcentaje(self, value: 2):
        self._descuentoPorcentaje = value

    @property
    def RecargoPorcentaje(self) -> float:
        return self._recargoPorcentaje

    @RecargoPorcentaje.setter
    def RecargoPorcentaje(self, value: 2):
        self._recargoPorcentaje = value

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NroLinDet=data.get('NroLinDet'),
            CdgItem=data.get('CdgItem'),
            IndExe=IndicadorFacturacionExencionEnum(data.get('IndExe')),
            Retenedor=Retenedor.from_dict(data.get('Retenedor')) if data.get('Retenedor') else None,
            NmbItem=data.get('NmbItem'),
            DscItem=data.get('DscItem'),
            QtyRef=data.get('QtyRef'),
            UnmdRef=data.get('UnmdRef'),
            PrcRef=data.get('PrcRef'),
            QtyItem=data.get('QtyItem'),
            Subcantidad=[SubCantidad.from_dict(subcantidad) for subcantidad in data.get('Subcantidad')] if data.get('Subcantidad') else None,
            FechaElaboracionString=data.get('FechaElaboracionString'),
            FechaVencimientoString=data.get('FechaVencimientoString'),
            UnmdItem=data.get('UnmdItem'),
            PrcItem=data.get('PrcItem'),
            OtrMnda=OtraMonedaDetalle.from_dict(data.get('OtrMnda')) if data.get('OtrMnda') else None,
            DescuentoPct=data.get('DescuentoPct'),
            recargo_monto=data.get('recargo_monto'),
            SubDscto=[SubDescuento.from_dict(subDscto) for subDscto in data.get('SubDscto')] if data.get('SubDscto') else None,
            RecargoPct=data.get('RecargoPct'),
            SubRecargo=[SubRecargo.from_dict(subRecargo) for subRecargo in data.get('SubRecargo')] if data.get('SubRecargo') else None,
            CodigoImpuestoAdicional=[TipoImpuestoEnum(codigoImpuestoAdicional) for codigoImpuestoAdicional in data.get('CodigoImpuestoAdicional')] if data.get('CodigoImpuestoAdicional') else None,
            MontoItem=data.get('MontoItem')
        )
    