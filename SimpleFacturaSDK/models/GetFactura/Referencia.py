from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import Enum

# Definición de las enumeraciones
class TipoReferenciaEnum(Enum):
    NOT_SET = "NotSet"
    # Agrega otros valores según sea necesario

@dataclass
class Referencia:
    """
    Clase que representa la referencia del documento.
    """

    NroLinRef: int = 0
    """Número secuencial de la referencia."""

    TpoDocRef: str = ''
    """Indica el tipo de documento siendo referenciado."""

    IndGlobal: int = 0
    """Indicador de referencia global."""

    FolioRef: str = ''
    """Identificación del documento siendo referenciado."""

    RUTOtr: str = ''
    """Sólo si el documento de referencia es de tipo tributario y fue emitido por otro contribuyente."""

    FechaDocumentoReferenciaString: str = ''
    """Fecha del documento siendo referenciado."""

    @property
    def FchRef(self) -> datetime:
        return datetime.strptime(self.FechaDocumentoReferenciaString, "%Y-%m-%d")

    @FchRef.setter
    def FchRef(self, value: datetime):
        self.FechaDocumentoReferenciaString = value.strftime("%Y-%m-%d")

    CodRef: TipoReferenciaEnum = TipoReferenciaEnum.NOT_SET
    """Código utilizado para los siguientes casos."""

    _razonReferencia: str = ''
    """Ejemplo: Una Nota de Crédito que hace referencia a una factura, indica "descuento por pronto pago" o "error en precio" etc."""

    @property
    def RazonRef(self) -> str:
        return self._razonReferencia

    @RazonRef.setter
    def RazonRef(self, value: str):
        self._razonReferencia = value[:90]  # Truncate to 90 characters

    def __init__(self):
        self.NroLinRef = 0
        self.TpoDocRef = ''
        self.FolioRef = ''
        self.FchRef = datetime.min
        self.IndGlobal = 0
        self.RUTOtr = ''
        self.CodRef = TipoReferenciaEnum.NOT_SET
        self.RazonRef = ''