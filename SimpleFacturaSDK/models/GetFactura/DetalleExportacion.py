from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CodigoItem
from SimpleFacturaSDK.enum.IndicadorFacturacionExencion import IndicadorFacturacionExencionEnum
from SimpleFacturaSDK.models.GetFactura.Retenedor import Retenedor
from SimpleFacturaSDK.models.GetFactura.SubCantidad import SubCantidad
from SimpleFacturaSDK.models.GetFactura.OtraMonedaDetalle import OtraMonedaDetalle
from SimpleFacturaSDK.models.GetFactura.SubDescuento import SubDescuento
from SimpleFacturaSDK.models.GetFactura.SubRecargo import SubRecargo
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
    def nmb_item(self) -> str:
        return self._nmb_item

    @nmb_item.setter
    def nmb_item(self, value: str):
        self._nmb_item = truncate(value, 80)

    @property
    def dsc_item(self) -> str:
        return self._dsc_item

    @dsc_item.setter
    def dsc_item(self, value: str):
        self._dsc_item = truncate(value, 1000)

    @property
    def qty_ref(self) -> float:
        return round(self._qty_ref, 6)

    @qty_ref.setter
    def qty_ref(self, value: float):
        self._qty_ref = value

    @property
    def prc_ref(self) -> float:
        return round(self._prc_ref, 6)

    @prc_ref.setter
    def prc_ref(self, value: float):
        self._prc_ref = value

    @property
    def qty_item(self) -> float:
        return round(self._qty_item, 6)

    @qty_item.setter
    def qty_item(self, value: float):
        self._qty_item = value

    @property
    def descuento_pct(self) -> float:
        return round(self._descuento_pct, 2)

    @descuento_pct.setter
    def descuento_pct(self, value: float):
        self._descuento_pct = value

    @property
    def recargo_pct(self) -> float:
        return round(self._recargo_pct, 2)

    @recargo_pct.setter
    def recargo_pct(self, value: float):
        self._recargo_pct = value

    @property
    def monto_item(self) -> float:
        return round(self._monto_item, 6)

    @monto_item.setter
    def monto_item(self, value: float):
        self._monto_item = value

    @property
    def fecha_elaboracion(self) -> Optional[str]:
        return self._fecha_elaboracion.strftime("%Y-%m-%d") if self._fecha_elaboracion else None

    @fecha_elaboracion.setter
    def fecha_elaboracion(self, value: datetime):
        self._fecha_elaboracion = value

    @property
    def fecha_vencimiento(self) -> Optional[str]:
        return self._fecha_vencimiento.strftime("%Y-%m-%d") if self._fecha_vencimiento else None

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, value: datetime):
        self._fecha_vencimiento = value


    def __init__(self):
        self.NroLinDet = 0
        self.NmbItem = ''
        self.MontoItem = 0.0
        self.CdgItem = []
        self.IndExe = IndicadorFacturacionExencionEnum.NOT_SET
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
