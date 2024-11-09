from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CodigoItem
from SimpleFacturaSDK.enumeracion.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.models.GetFactura.Retenedor import Retenedor
from SimpleFacturaSDK.models.GetFactura.SubCantidad import SubCantidad
from SimpleFacturaSDK.models.GetFactura.OtraMonedaDetalle import OtraMonedaDetalle
from SimpleFacturaSDK.models.GetFactura.SubDescuento import SubDescuento
from SimpleFacturaSDK.models.GetFactura.SubRecargo import SubRecargo
from SimpleFacturaSDK.enumeracion.TipoImpuesto import TipoImpuestoEnum



def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class DetalleExportacion:
    NroLinDet: int = 0
    CdgItem: Optional[List[CodigoItem]] = None
    IndExe: IndicadorFacturacionExencionEnum = IndicadorFacturacionExencionEnum.NotSet
    Retenedor: Optional[Retenedor] = None
    NmbItem: str = ""
    DscItem: str = ""
    QtyRef: float = 0.0
    UnmdRef: str = ""
    PrcRef: float = 0.0
    QtyItem: float = 0.0
    Subcantidad: Optional[List[SubCantidad]] = None
    FechaElaboracionString: str = ""
    FchElabor = datetime.now() 
    FechaVencimientoString: str = ""
    FchVenc = datetime.now()
    UnmdItem: str = ""
    PrcItem: float = 0.0
    OtrMnda: Optional[OtraMonedaDetalle] = None
    DescuentoPct: float = 0.0
    DescuentoMonto: int = 0
    SubDscto: Optional[List[SubDescuento]] = None
    RecargoPct: float = 0.0
    RecargoMonto: int = 0
    SubRecargo: Optional[List[SubRecargo]] = None
    CodigoImpuestoAdicional: Optional[List[TipoImpuestoEnum]] = None
    MontoItem: float = 0.0



    __nombre: str = field(default="", init=False, metadata={"max_length": 80})
    __descripcion: str = field(default="", init=False, metadata={"max_length": 1000})
    __cantidadUnidadMedidaReferencia: float = field(default=0.0, init=False, metadata={"decimals": 6})
    __unidadMedidaReferencia: str = field(default="", init=False, metadata={"max_length": 4})
    __precioUnitarioUnidadMedidaReferencia: float = field(default=0.0, init=False, metadata={"decimals": 6})
    __cantidad: float = field(default=0.0, init=False, metadata={"decimals": 6})
    __unidadMedida: str = field(default="", init=False, metadata={"max_length": 4})
    __precio: float = field(default=0.0, init=False)
    __descuentoPorcentaje: float = field(default=0.0, init=False, metadata={"decimals": 2})
    __recargoPorcentaje: float = field(default=0.0, init=False, metadata={"decimals": 2})
    __montoItem: float = field(default=0.0, init=False, metadata={"decimals": 6})

    def __post_init__(self):
        self.FchVenc = datetime.strptime(self.FechaVencimientoString, "%Y-%m-%d") if self.FechaVencimientoString else None
        self.FchElabor = datetime.strptime(self.FechaElaboracionString, "%Y-%m-%d") if self.FechaElaboracionString else None
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
        self.__montoItem = round(self.MontoItem, 6)



    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            NroLinDet=data.get('NroLinDet'),
            CdgItem=[CodigoItem.from_dict(item) for item in data.get('CdgItem')],
            IndExe=IndicadorFacturacionExencionEnum(data.get('IndExe')),
            Retenedor=Retenedor.from_dict(data.get('Retenedor')),
            NmbItem=data.get('NmbItem'),
            DscItem=data.get('DscItem'),
            QtyRef=data.get('QtyRef'),
            UnmdRef=data.get('UnmdRef'),
            PrcRef=data.get('PrcRef'),
            QtyItem=data.get('QtyItem'),
            Subcantidad=[SubCantidad.from_dict(item) for item in data.get('Subcantidad')],
            FechaElaboracionString=data.get('FechaElaboracionString'),
            FchElabor=data.get('FchElabor'),
            FechaVencimientoString=data.get('FechaVencimientoString'),
            FchVenc=data.get('FchVenc'),
            UnmdItem=data.get('UnmdItem'),
            PrcItem=data.get('PrcItem'),
            OtrMnda=OtraMonedaDetalle.from_dict(data.get('OtrMnda')),
            DescuentoPct=data.get('DescuentoPct'),
            DescuentoMonto=data.get('DescuentoMonto'),
            SubDscto=[SubDescuento.from_dict(item) for item in data.get('SubDscto')],
            RecargoPct=data.get('RecargoPct'),
            RecargoMonto=data.get('RecargoMonto'),
            SubRecargo=[SubRecargo.from_dict(item) for item in data.get('SubRecargo')],
            CodigoImpuestoAdicional=[TipoImpuestoEnum(item) for item in data.get('CodigoImpuestoAdicional')],
            MontoItem=data.get('MontoItem')
        )




