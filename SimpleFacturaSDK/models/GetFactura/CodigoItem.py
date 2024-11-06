from dataclasses import dataclass

@dataclass
class CodigoItem:
    """
    Clase que representa el código del item.
    """

    _tipoCodigo: str = ''
    """Tipo de codificación utilizada para el item."""

    _valorCodigo: str = ''
    """Valor del código para TipoCodigo."""

    @property
    def TpoCodigo(self) -> str:
        return self._tipoCodigo

    @TpoCodigo.setter
    def TpoCodigo(self, value: str):
        self._tipoCodigo = value[:10]  # Truncate to 10 characters

    @property
    def VlrCodigo(self) -> str:
        return self._valorCodigo

    @VlrCodigo.setter
    def VlrCodigo(self, value: str):
        self._valorCodigo = value[:35]  # Truncate to 35 characters

    def __init__(self):
        self.TpoCodigo = ''
        self.VlrCodigo = ''