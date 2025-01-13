from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class DteClass:
    folio: int
    tipoDTE: int 

@dataclass
class MailClass:
    to: List[str]
    ccos: List[str]
    ccs: List[str]

@dataclass
class EnvioMailRequest:
    RutEmpresa: str
    Dte: DteClass
    Mail: MailClass
    Xml: bool
    Pdf: bool 
    Comments: Optional[str]

