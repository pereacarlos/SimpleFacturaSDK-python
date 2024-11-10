from dataclasses import dataclass, field
from datetime import datetime

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class MontoPagoItem:
    FchPago: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    MntPago: int
    Glosa: str
    __glosa: str 

    def __post_init__(self):
        self.__glosa = truncate(self.Glosa, 40)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            FchPago=data.get('FchPago'),
            MntPago=data.get('MntPago'),
            Glosa=data.get('Glosa')
        )
