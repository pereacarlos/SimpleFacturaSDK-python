from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class EnvioMailRequest:
    RutEmpresa: str
    Dte: DteClass
    Mail: MailClass
    Xml: bool
    Pdf: bool 
    Comments: Optional[str]

@dataclass
class DteClass:
    folio: int
    tipoDTE: int 

@dataclass
class MailClass:
    to: List[str]
    ccos: List[str]
    ccs: List[str]


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            RutEmpresa=data.get('RutEmpresa'),
            Dte=DteClass(**data.get('Dte', {})),
            Mail=MailClass(**data.get('Mail', {})),
            Xml=data.get('Xml', False),
            Pdf=data.get('Pdf', False),
            Comments=data.get('Comments'),
            folio=data.get('folio'),
            tipoDTE=data.get('tipoDTE'),
            to=data.get('to'),
            ccos=data.get('ccos'),
            ccs=data.get('ccs')
        )

    def to_dict(self):
        return {
            'RutEmpresa': self.RutEmpresa,
            'Dte': self.Dte.__dict__,
            'Mail': self.Mail.__dict__,
            'Xml': self.Xml,
            'Pdf': self.Pdf,
            'Comments': self.Comments
        }