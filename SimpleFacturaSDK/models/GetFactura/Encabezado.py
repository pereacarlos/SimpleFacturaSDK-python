from dataclasses import dataclass, field
from typing import Optional
from IdentificacionDTE import IdentificacionDTE
from Emisor import Emisor
from Receptor import Receptor
from Transporte import Transporte
from Totales import Totales
from OtraMoneda import OtraMoneda

@dataclass
class Encabezado:
    """
    Clase que representa el encabezado del documento.
    """

    IdDoc: IdentificacionDTE = field(default_factory=IdentificacionDTE)
    """Identificación y totales del documento."""

    Emisor: Emisor = field(default_factory=Emisor)
    """Datos del emisor."""

    RUTMandante: Optional[str] = field(default='')
    """
    Rut a cuenta de quien se emite el DTE.
    Corresponde al RUT del mandante si el total de la venta o servicio es por cuenta de otro el cual es responsable del IVA devengado en el período.
    Con guión y dígito verificador.
    """

    Receptor: Receptor = field(default_factory=Receptor)
    """Datos del receptor."""

    RUTSolicita: Optional[str] = field(default='')
    """
    Rut que solicita el DTE en venta a público.
    En casos de venta a público. Es obligatorio si es distinto de Rut receptor o Rut Receptor es persona jurídica.
    Con guión y dígito verificador.
    """

    Transporte: Optional[Transporte] = None
    """Información de transporte de mercaderías."""

    Totales: Totales = field(default_factory=Totales)
    """Montos totales del DTE."""

    OtraMoneda: Optional[OtraMoneda] = None
    """Otra moneda."""

    def __init__(self):
        self.RUTMandante = ''
        self.RUTSolicita = ''
        self.IdDoc = IdentificacionDTE()
        self.Emisor = Emisor()
        self.Receptor = Receptor()
        self.Transporte = None
        self.Totales = Totales()
        self.OtraMoneda = None