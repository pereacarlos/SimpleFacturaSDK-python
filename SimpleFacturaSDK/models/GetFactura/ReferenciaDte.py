from dataclasses import dataclass, field
from datetime import datetime
from SimpleFacturaSDK.Enum.TipoDTE import DTEType


@dataclass
class ReferenciaDte:
    fecha: str = field(default="")
    motivo: str = field(default="")
    razon: str = field(default="")
    glosa: str = field(default="")
    folio: int = field(default=0)
    tipo_doc: DTEType = field(default=DTEType.NotSet)  # Ajusta NotSet según los valores de tu enumeración en DTEType

    @property
    def fch_ref(self) -> datetime:
        """Convierte la fecha en string a datetime cuando se accede a fch_ref."""
        return datetime.strptime(self.fecha, "%Y-%m-%d") if self.fecha else None

    @fch_ref.setter
    def fch_ref(self, value: datetime):
        """Establece la fecha en formato string a partir de un objeto datetime."""
        self.fecha = value.strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "fecha": self.fecha,
            "motivo": self.motivo,
            "razon": self.razon,
            "glosa": self.glosa,
            "folio": self.folio,
            "tipoDoc": self.tipo_doc.name  # Cambia a .value si necesitas el valor numérico de la enumeración
        }
