from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field, asdict
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoSalida import TipoSalidaEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class ListaDteRequestEnt:
    Credenciales: Credenciales
    ambiente: AmbienteEnum
    salida: Optional[TipoSalidaEnum] = None
    folio: Optional[float] = None
    codigoTipoDte: Optional[DTEType] = None
    desde: Optional[datetime] = None
    hasta: Optional[datetime] = None
    rutEmisor: Optional[str] = None

    def to_dict(self):
        return asdict(self)