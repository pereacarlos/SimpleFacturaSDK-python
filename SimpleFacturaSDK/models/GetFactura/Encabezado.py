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
    IdDoc: IdentificacionDTE = field(default_factory=IdentificacionDTE)
    Emisor: Emisor = field(default_factory=Emisor)
    RUTMandante: Optional[str] = field(default='')
    Receptor: Receptor = field(default_factory=Receptor)
    RUTSolicita: Optional[str] = field(default='')
    Transporte: Optional[Transporte] = None
    Totales: Totales = field(default_factory=Totales)
    OtraMoneda: Optional[OtraMoneda] = None    


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            IdDoc=IdentificacionDTE.from_dict(data.get('IdDoc')),
            Emisor=Emisor.from_dict(data.get('Emisor')),
            RUTMandante=data.get('RUTMandante', ''),
            Receptor=Receptor.from_dict(data.get('Receptor')),
            RUTSolicita=data.get('RUTSolicita', ''),
            Transporte=Transporte.from_dict(data.get('Transporte')) if data.get('Transporte') else None,
            Totales=Totales.from_dict(data.get('Totales')),
            OtraMoneda=OtraMoneda.from_dict(data.get('OtraMoneda')) if data.get('OtraMoneda') else None
        )
        

    def to_dict(self):
        return asdict(self)