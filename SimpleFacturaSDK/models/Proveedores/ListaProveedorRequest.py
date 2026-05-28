from dataclasses import dataclass
from SimpleFacturaSDK.enumeracion.ListaProveedorEnum import ListaProveedorEnum
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales


@dataclass
class ListaProveedorRequest:
    Credenciales: Credenciales
    RutProveedor: str
    ListaProveedor: ListaProveedorEnum


    def to_dict(self):
          return {
            "credenciales": self.Credenciales.to_dict(),
            "rutProveedor": self.RutProveedor,
            "listaProveedor" : self.ListaProveedor.value if self.ListaProveedor else None
        }