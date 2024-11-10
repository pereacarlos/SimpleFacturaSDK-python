from dataclasses import dataclass, field
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdentificacionDTE
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda

@dataclass
class Encabezado:
    IdDoc: IdentificacionDTE
    Emisor: Emisor
    RUTMandante: Optional[str]
    Receptor: Receptor
    RUTSolicita: Optional[str]
    Transporte: Optional[Transporte]
    Totales: Totales
    OtraMoneda: Optional[OtraMoneda]   


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            IdDoc=IdentificacionDTE,
            Emisor=Emisor,
            RUTMandante=data.get('RUTMandante'),
            Receptor=Receptor,
            RUTSolicita=data.get('RUTSolicita'),
            Transporte=Transporte,
            Totales=Totales,
            OtraMoneda=OtraMoneda
        )
        

    def to_dict(self):
        return asdict(self)