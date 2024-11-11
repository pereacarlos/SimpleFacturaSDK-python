from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Documento import Documento


@dataclass
class RequestDTE:
    Documento: Documento
    Observaciones: str
    TipoPago: str
