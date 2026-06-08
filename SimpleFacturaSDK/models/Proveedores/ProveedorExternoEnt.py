from dataclasses import dataclass
from typing import Optional

from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum


@dataclass
class ProveedorExternoEnt:
    rut: str = ""
    razonSocial: str = ""
    giro: str = ""
    dirFact: str = ""
    correoPar: str = ""
    ciudad: str = ""
    comuna: str = ""
    correoFact: Optional[str] = None
    listaProveedor: str = ""
    activo: bool = False

    @classmethod
    def from_dict(cls, data: dict):
        lista_proveedor = data.get("listaProveedor", data.get("ListaProveedor", ""))
        if isinstance(lista_proveedor, int):
            try:
                lista_proveedor = ListaProveedorEnum(lista_proveedor).name
            except ValueError:
                lista_proveedor = str(lista_proveedor)

        return cls(
            rut=data.get("rut", data.get("Rut", "")),
            razonSocial=data.get("razonSocial", data.get("RazonSocial", "")),
            giro=data.get("giro", data.get("Giro", "")),
            dirFact=data.get("dirFact", data.get("DirFact", "")),
            correoPar=data.get("correoPar", data.get("CorreoPar", "")),
            ciudad=data.get("ciudad", data.get("Ciudad", "")),
            comuna=data.get("comuna", data.get("Comuna", "")),
            correoFact=data.get("correoFact", data.get("CorreoFact")),
            listaProveedor=lista_proveedor,
            activo=data.get("activo", data.get("Activo", False)),
        )

    def to_dict(self):
        return {
            "rut": self.rut,
            "razonSocial": self.razonSocial,
            "giro": self.giro,
            "dirFact": self.dirFact,
            "correoPar": self.correoPar,
            "ciudad": self.ciudad,
            "comuna": self.comuna,
            "correoFact": self.correoFact,
            "listaProveedor": self.listaProveedor,
            "activo": self.activo,
        }


@dataclass
class NuevoProveedorExternoEnt:
    Rut: str
    RazonSocial: str
    Giro: str
    DirFact: str
    CorreoPar: str
    Ciudad: str
    Comuna: str
    CorreoFact: Optional[str] = None
    ListaProveedor: ListaProveedorEnum = ListaProveedorEnum.Desconocido

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "RazonSocial": self.RazonSocial,
            "Giro": self.Giro,
            "DirFact": self.DirFact,
            "CorreoPar": self.CorreoPar,
            "Ciudad": self.Ciudad,
            "Comuna": self.Comuna,
            "CorreoFact": self.CorreoFact,
            "ListaProveedor": self.ListaProveedor.value if self.ListaProveedor else None,
        }


@dataclass
class EditarProveedorExternoEnt:
    Rut: str
    RazonSocial: Optional[str] = None
    Giro: Optional[str] = None
    DirFact: Optional[str] = None
    CorreoPar: Optional[str] = None
    Ciudad: Optional[str] = None
    Comuna: Optional[str] = None
    CorreoFact: Optional[str] = None
    ListaProveedor: Optional[ListaProveedorEnum] = None

    def to_dict(self):
        return {
            "Rut": self.Rut,
            "RazonSocial": self.RazonSocial,
            "Giro": self.Giro,
            "DirFact": self.DirFact,
            "CorreoPar": self.CorreoPar,
            "Ciudad": self.Ciudad,
            "Comuna": self.Comuna,
            "CorreoFact": self.CorreoFact,
            "ListaProveedor": self.ListaProveedor.value if self.ListaProveedor else None,
        }
