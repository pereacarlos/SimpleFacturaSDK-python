from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
@dataclass
class FolioRequest:
    def __init__(self, credenciales: Credenciales, cantidad: int, codigo_tipo_dte: Optional[DTEType] = None, ambiente: Optional[int] = None):
        self.credenciales = credenciales
        self.cantidad = cantidad
        self.codigo_tipo_dte = codigo_tipo_dte
        self.ambiente = ambiente

    def to_dict(self):
        return {
            "credenciales": self.credenciales.to_dict(),
            "cantidad": self.cantidad,
            "codigo_tipo_dte": self.codigo_tipo_dte,
            "ambiente": self.ambiente
        }


'''
from dataclasses import dataclass
from typing import Optional
from SDKSimpleFactura.Models.Facturacion import Credenciales
from SDKSimpleFactura.Enum.TipoDTE import DTEType

@dataclass
class FolioRequest:
    credenciales: Credenciales
    cantidad: int
    codigo_tipo_dte: Optional[DTEType] = None
    ambiente: Optional[int] = None'''