from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field, asdict
from enumeracion.Ambiente import AmbienteEnum
from models.GetFactura.Credenciales import Credenciales
from enumeracion.TipoSalida import TipoSalidaEnum
from enumeracion.TipoDTE import DTEType
from models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

@dataclass
class ListaDteRequestEnt:
    Credenciales: Credenciales
    ambiente: Optional[AmbienteEnum] = None
    salida: Optional[TipoSalidaEnum] = None
    folio: Optional[float] = None
    codigoTipoDte: Optional[DTEType] = None
    desde: Optional[datetime] = None
    hasta: Optional[datetime] = None
    rutEmisor: Optional[str] = None


    def to_dict(self):
          return {
            "credenciales": self.Credenciales.to_dict(),
            "ambiente": self.ambiente.value if self.ambiente else None,
            "folio": self.folio,
            "codigoTipoDte": self.codigoTipoDte.value if self.codigoTipoDte else None,
            "desde": self.desde.strftime("%Y-%m-%d") if self.desde else None,
            "hasta": self.hasta.strftime("%Y-%m-%d") if self.hasta else None,
            "rutEmisor": self.rutEmisor

        }