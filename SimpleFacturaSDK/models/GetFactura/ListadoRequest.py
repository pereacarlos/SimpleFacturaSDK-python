from datetime import datetime
from typing import Optional
from dataclasses import dataclass, field, asdict
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.CredencialExterna import CredencialExternaEnt
from SimpleFacturaSDK.enumeracion.TipoSalida import TipoSalidaEnum
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

@dataclass
class ListaDteRequestEnt:
    Credenciales: CredencialExternaEnt
    ambiente: AmbienteEnum.Certificacion
    folio: Optional[float]
    codigoTipoDte: Optional[DTEType.NotSet]
    desde: Optional[datetime]
    hasta: Optional[datetime]
    salida: TipoSalidaEnum.Base64
    rutEmisor: Optional[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Credenciales=CredencialExternaEnt.from_dict(data.get('Credenciales')),
            ambiente=AmbienteEnum(data.get('ambiente')),
            folio=data.get('folio'),
            codigoTipoDte=DTEType(data.get('codigoTipoDte')),
            desde=data.get('desde'),
            hasta=data.get('hasta'),
            salida=TipoSalidaEnum(data.get('salida')),
            rutEmisor=data.get('rutEmisor')
        )

    def to_dict(self):
        return asdict(self)
