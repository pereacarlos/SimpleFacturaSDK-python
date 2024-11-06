from dataclasses import dataclass

@dataclass
class SubCantidad:
    """
    Clase que representa la subcantidad del documento.
    """

    SubQty: float = 0.0
    """Cantidad distribuida."""

    _codigo: str = ''
    """Código descriptivo de la subcantidad."""

    @property
    def SubCod(self) -> str:
        return self._codigo

    @SubCod.setter
    def SubCod(self, value: str):
        self._codigo = value[:35]  # Truncate to 35 characters

    def __init__(self):
        self.SubQty = 0.0
        self.SubCod = ''