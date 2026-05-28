from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union

from SimpleFacturaSDK.enumeracion.Ambiente import AmbienteEnum
from SimpleFacturaSDK.enumeracion.PlanUsuario import PlanUsuarioEnum


@dataclass
class EmisorReq:
    RutEmpresa: str = ""
    RazonSocial: str = ""
    RutRepresentanteLegal: str = ""
    Giro: str = ""
    Email: str = ""
    DireccionFacturacion: str = ""
    Ciudad: str = ""
    Comuna: str = ""
    Telefono: Optional[str] = None
    FechaResolucion: Optional[datetime] = None
    NumeroResolucion: int = 0
    Ambiente: AmbienteEnum = AmbienteEnum.Certificacion
    PasswordSii: Optional[str] = None
    UnidadSii: str = ""

    def to_dict(self):
        return {
            "rutEmpresa": self.RutEmpresa,
            "razonSocial": self.RazonSocial,
            "rutRepresentanteLegal": self.RutRepresentanteLegal,
            "giro": self.Giro,
            "email": self.Email,
            "direccionFacturacion": self.DireccionFacturacion,
            "ciudad": self.Ciudad,
            "comuna": self.Comuna,
            "telefono": self.Telefono,
            "fechaResolucion": self.FechaResolucion.isoformat() if isinstance(self.FechaResolucion, datetime) else self.FechaResolucion,
            "numeroResolucion": self.NumeroResolucion,
            "ambiente": self.Ambiente.value if isinstance(self.Ambiente, AmbienteEnum) else self.Ambiente,
            "passwordSii": self.PasswordSii,
            "unidadSii": self.UnidadSii,
        }


@dataclass
class SucursalReq:
    Nombre: str = "Casa Matriz"
    Direccion: str = "Direccion 1"

    def to_dict(self):
        return {
            "nombre": self.Nombre,
            "direccion": self.Direccion,
        }


@dataclass
class WizardEmisorRequest:
    Emisor: EmisorReq = field(default_factory=EmisorReq)
    Sucursal: SucursalReq = field(default_factory=SucursalReq)
    ActividadesEconomicas: List[int] = field(default_factory=list)
    Plan: PlanUsuarioEnum = PlanUsuarioEnum.Independiente

    def to_dict(self):
        return {
            "emisor": self.Emisor.to_dict(),
            "sucursal": self.Sucursal.to_dict(),
            "actividadesEconomicas": self.ActividadesEconomicas,
            "plan": self.Plan.value if isinstance(self.Plan, PlanUsuarioEnum) else self.Plan,
        }
