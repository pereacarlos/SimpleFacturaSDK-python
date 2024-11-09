from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType


@dataclass
class ReferenciaDte:
    fecha: str = field(default="")
    motivo: str = field(default="")
    razon: str = field(default="")
    glosa: str = field(default="")
    folio: int = field(default=0)
    tipo_doc: DTEType = field(default=DTEType.NotSet) 

    @property
    def fch_ref(self) -> datetime:
        return datetime.strptime(self.fecha, "%Y-%m-%d") if self.fecha else None

    @fch_ref.setter
    def fch_ref(self, value: datetime):
        self.fecha = value.strftime("%Y-%m-%d")

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
