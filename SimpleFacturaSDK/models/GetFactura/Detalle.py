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
    __nombre: str = field(init=False, default="", metadata={"max_length": 80})
    __descripcion: str = field(init=False, default="", metadata={"max_length": 1000})
    __cantidadUnidadMedidaReferencia: float = field(init=False, default=0.0, metadata={"decimals": 6})
    __unidadMedidaReferencia: str = field(init=False, default="", metadata={"max_length": 4})
    __precioUnitarioUnidadMedidaReferencia: float = field(init=False, default=0.0, metadata={"decimals": 6})
    __cantidad: float = field(init=False, default=0.0, metadata={"decimals": 6})
    __unidadMedida: str = field(init=False, default="", metadata={"max_length": 4})
    __precio: float = field(init=False, default=0.0)
    __descuentoPorcentaje: float = field(init=False, default=0.0, metadata={"decimals": 2})
    __recargoPorcentaje: float = field(init=False, default=0.0, metadata={"decimals": 2})

    def __post_init__(self):
        self.__nombre = truncate(self.NmbItem, 80)
        self.__descripcion = truncate(self.DscItem, 1000)
        self.__cantidadUnidadMedidaReferencia = round(self.QtyRef, 6)
        self.__unidadMedidaReferencia = truncate(self.UnmdRef, 4)
        self.__precioUnitarioUnidadMedidaReferencia = round(self.PrcRef, 6)
        self.__cantidad = round(self.QtyItem, 6)
        self.__unidadMedida = truncate(self.UnmdItem, 4)
        self.__precio = self.PrcItem
        self.__descuentoPorcentaje = round(self.DescuentoPct, 2)
        self.__recargoPorcentaje = round(self.RecargoPct, 2)


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
    