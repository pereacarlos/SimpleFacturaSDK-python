from typing import Optional
from dataclasses import dataclass
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from datetime import datetime

@dataclass
class ListaBHERequest:
    credenciales: Credenciales
    Folio: Optional[int] = None
    Desde: Optional[datetime] = None
    Hasta: Optional[datetime] = None

