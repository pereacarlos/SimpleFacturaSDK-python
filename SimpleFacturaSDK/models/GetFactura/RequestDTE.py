from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.enumeracion.TipoDTE import TipoDTE
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicio


@dataclass
class RequestDTE:
    Documento: Optional[Documento] = field(default_factory=Documento)
    Exportaciones: Optional[Exportaciones] = None
    Observaciones: Optional[str] = None
    Cajero: Optional[str] = None
    TipoPago: Optional[str] = None
    Propina: Optional[int] = None

    def __init__(self, emisor: Optional[Emisor] = None, receptor: Optional[Receptor] = None, folio: Optional[int] = None, tipo: Optional[TipoDTE] = None):
        if emisor and receptor and folio and tipo:
            self.Documento = Documento()
            self.Documento.Encabezado.Emisor = emisor
            self.Documento.Encabezado.Receptor = receptor
            self.Documento.Encabezado.IdDoc.Folio = folio
            self.Documento.Encabezado.IdDoc.TipoDTE = tipo
            self.Documento.Encabezado.IdDoc.FchEmis = datetime.now()

            if tipo in [TipoDTE.DTEType.BoletaElectronica, TipoDTE.DTEType.BoletaElectronicaExenta]:
                self.documento.encabezado.id_doc.ind_servicio = IndicadorServicio.IndicadorServicioEnum.BoletaVentasYServicios

        else:
            self.Documento = None