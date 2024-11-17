from dataclasses import dataclass
from typing import Optional
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from enumeracion.ResponseType import ResponseType
from enumeracion.RejectionType import RejectionType

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

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "dte_referenciado_externo": self.dte_referenciado_externo.to_dict(),
            "respuesta": self.respuesta.value,
            "tipo_rechazo": self.tipo_rechazo.value if self.tipo_rechazo else None,
            "comentario": self.comentario
        }