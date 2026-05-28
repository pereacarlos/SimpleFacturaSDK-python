from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union

from SimpleFacturaSDK.enumeracion.TipoRetencion import TipoRetencion
from SimpleFacturaSDK.models.BoletaHonorarios.BasicData import BasicData


@dataclass
class Receptor:
    Rut: str = ""
    Nombre: str = ""
    Direccion: str = ""
    Comuna: str = ""
    Region: int = 0

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "Nombre": self.Nombre,
            "Direccion": self.Direccion,
            "Comuna": self.Comuna,
            "Region": self.Region,
        }


@dataclass
class Emisor:
    Rut: Optional[str] = None
    Direccion: Optional[Union[int, str]] = None

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "Direccion": self.Direccion,
        }


@dataclass
class Detalle:
    Nombre: str = ""
    Valor: int = 0

    def to_dict(self):
        return {
            "Nombre": self.Nombre,
            "Valor": self.Valor,
        }


@dataclass
class BHData(BasicData):
    RutEmisor: str = ""
    Correo: Optional[str] = ""
    Retencion: TipoRetencion = TipoRetencion.Receptor
    FechaEmision: str = field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y"))
    Receptor: Receptor = field(default_factory=Receptor)
    Emisor: Emisor = field(default_factory=Emisor)
    Detalles: List[Detalle] = field(default_factory=list)
    Folio: Optional[int] = 0
    Observacion: Optional[str] = ""

    def to_dict(self):
        return {
            "RutEmisor": self.RutEmisor,
            "Correo": self.Correo,
            "Retencion": self.Retencion.value if isinstance(self.Retencion, TipoRetencion) else self.Retencion,
            "FechaEmision": self.FechaEmision,
            "Receptor": self.Receptor.to_dict() if self.Receptor else None,
            "Emisor": self.Emisor.to_dict() if self.Emisor else None,
            "Detalles": [detalle.to_dict() for detalle in self.Detalles],
            "Folio": self.Folio,
            "Observacion": self.Observacion,
        }
