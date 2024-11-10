from datetime import datetime
from typing import Optional
from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.models.GetFactura.CredencialExterna import CredencialExternaEnt
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType

class ListaDteRequestEnt:
    Credenciales: CredencialExternaEnt
    Ambiente: AmbienteEnum.Certificacion
    Folio: Optional[float]
    CodigoTipoDte: Optional[DTEType.NotSet]
    Desde: Optional[datetime]
    Hasta: Optional[datetime]
    Salida: TipoSalidaEnum.NotSet
    RutEmisor: Optional[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Credenciales=CredencialExternaEnt.from_dict(data.get('Credenciales')),
            Ambiente=AmbienteEnum(data.get('ambiente')),
            Folio=data.get('folio'),
            CodigoTipoDte=DTEType(data.get('codigoTipoDte')),
            Desde=data.get('desde'),
            Hasta=data.get('hasta'),
            Salida=TipoSalidaEnum(data.get('Salida')),
            RutEmisor=data.get('RutEmisor')
        )

