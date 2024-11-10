from dataclasses import dataclass
from typing import Optional
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.enumeracion.ResponseType import ResponseType
from SimpleFacturaSDK.enumeracion.RejectionType import RejectionType

@dataclass
class AcuseReciboExternoRequest:
    credenciales: Credenciales
    dte_referenciado_externo: DteReferenciadoExterno
    respuesta: ResponseType
    tipo_rechazo: Optional[RejectionType] 
    comentario: Optional[str] 

    @classmethod
    def from_dict(cls, dict) -> 'AcuseReciboExternoRequest':
        return AcuseReciboExternoRequest(
            credenciales = Credenciales,
            dte_referenciado_externo = DteReferenciadoExterno,
            respuesta = ResponseType(dict['respuesta']),
            tipo_rechazo = RejectionType(dict['tipo_rechazo']) if dict.get('tipo_rechazo') else None,
            comentario = dict.get('comentario')
        )