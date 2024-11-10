from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType


@dataclass
class ReferenciaDte:
    fecha: str 
    FchRef: datetime
    motivo: str
    razon: str
    glosa: str 
    folio: int 
    tipo_doc: DTEType

    def __post_init__(self):
        self.FchRef = datetime.strptime(self.fecha, "%Y-%m-%d")


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fecha=data.get('fecha'),
            motivo=data.get('motivo'),
            razon=data.get('razon'),
            glosa=data.get('glosa'),
            folio=data.get('folio'),
            tipo_doc=DTEType(data.get('tipoDoc'))
        )

    def to_dict(self):
        return {
            "fecha": self.fecha,
            "motivo": self.motivo,
            "razon": self.razon,
            "glosa": self.glosa,
            "folio": self.folio,
            "tipoDoc": self.tipo_doc.name 
        }
