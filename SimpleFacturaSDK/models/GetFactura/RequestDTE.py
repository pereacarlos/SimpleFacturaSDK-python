from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.enumeracion.TipoDTE import DOCType, DTEType, DTEFacturasType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum, IndicadorServicioDetalleLibroEnum


@dataclass
class RequestDTE:
    Documento: Optional[Documento] = field(default_factory=Documento)
    Exportaciones: Optional[Exportaciones] = None
    Observaciones: Optional[str] = None
    Cajero: Optional[str] = None
    TipoPago: Optional[str] = None
    Propina: Optional[int] = None

    def __init__(self, documento: Optional[Documento] = None, emisor: Optional[Emisor] = None, receptor: Optional[Receptor] = None, folio: Optional[int] = None, TipoDTE: Optional[DTEType] = None, Observaciones: Optional[str] = None, Cajero: Optional[str] = None, TipoPago: Optional[str] = None, Propina: Optional[int] = None):
        if emisor and receptor and folio and tipo:
            self.Documento = documento
            self.Documento.Encabezado.Emisor = emisor
            self.Documento.Encabezado.Receptor = receptor
            self.Documento.Encabezado.IdDoc.Folio = folio
            self.Documento.Encabezado.IdDoc.TipoDTE = tipo
            self.Documento.Encabezado.IdDoc.FchEmis = datetime.now()

            if tipo in [DTEType.BoletaElectronica, DTEType.BoletaElectronicaExenta]:
                self.Documento.Encabezado.IdDoc.IndServicio = IndicadorServicioEnum.BoletaVentasYServicios

        else:
            self.Documento = None


    def to_dict(self):
        return {
            "Documento": self.Documento.to_dict() if self.Documento else None,
            "Exportaciones": self.Exportaciones.to_dict() if self.Exportaciones else None,
            "Observaciones": self.Observaciones,
            "Cajero": self.Cajero,
            "TipoPago": self.TipoPago,
            "Propina": self.Propina
        }