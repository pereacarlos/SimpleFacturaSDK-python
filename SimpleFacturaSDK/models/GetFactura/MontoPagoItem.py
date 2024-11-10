from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class MontoPagoItem:
    MntPago: int
    Glosa: str
    FchPago: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    __glosa: str = field(init=False)

    def __post_init__(self):
        self.__glosa = self.truncate(self.Glosa, 40)

    @staticmethod
    def truncate(value: str, max_length: int) -> str:
        return value if len(value) <= max_length else value[:max_length]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            FchPago=data.get('FchPago', datetime.min.strftime("%Y-%m-%d")),
            MntPago=data.get('MntPago'),
            Glosa=data.get('Glosa')
        )

    def to_dict(self):
        return {
            'FchPago': self.FchPago,
            'MntPago': self.MntPago,
            'Glosa': self.Glosa
        }