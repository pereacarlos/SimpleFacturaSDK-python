from dataclasses import dataclass, field
from datetime import datetime

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class MontoPagoItem:
    FchPago: str = field(default_factory=lambda: datetime.min.strftime("%Y-%m-%d"))
    MntPago: int = 0
    _glosa: str = field(default="", init=False)

    @property
    def GlosaPagos(self) -> str:
        return self._glosa

    @GlosaPagos.setter
    def GlosaPagos(self, value: str):
        self._glosa = truncate(value, 40)

    @property
    def FchPagoDate(self) -> datetime:
        """Permite obtener `FchPago` como un objeto `datetime`."""
        return datetime.strptime(self.FchPago, "%Y-%m-%d")

    @FchPagoDate.setter
    def FchPagoDate(self, value: datetime):
        """Permite establecer `FchPago` utilizando un objeto `datetime`."""
        self.FchPago = value.strftime("%Y-%m-%d")
