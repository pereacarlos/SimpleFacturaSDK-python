from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class CdgItem:
    TpoCodigo: str
    VlrCodigo: str