from dataclasses import dataclass

@dataclass
class OtraMonedaDetalle:
    """
    Clase que representa los detalles en otra moneda del documento.
    """

    _precioUnitario: float = 0.0
    """Precio unitario en otra moneda."""

    Moneda: str = ''
    """Código de otra moneda."""

    _factorConversion: float = 0.0
    """Factor para conversión a pesos."""

    _descuento: float = 0.0
    """Descuento en otra moneda."""

    _recargo: float = 0.0
    """Recargo en otra moneda."""

    _valor: float = 0.0
    """Valor por línea de detalle en otra moneda."""

    @property
    def PrcOtrMon(self) -> float:
        return round(self._precioUnitario, 4)

    @PrcOtrMon.setter
    def PrcOtrMon(self, value: float):
        self._precioUnitario = value

    @property
    def FctConv(self) -> float:
        return round(self._factorConversion, 4)

    @FctConv.setter
    def FctConv(self, value: float):
        self._factorConversion = value

    @property
    def DctoOtrMnda(self) -> float:
        return round(self._descuento, 4)

    @DctoOtrMnda.setter
    def DctoOtrMnda(self, value: float):
        self._descuento = value

    @property
    def RecargoOtrMnda(self) -> float:
        return round(self._recargo, 4)

    @RecargoOtrMnda.setter
    def RecargoOtrMnda(self, value: float):
        self._recargo = value

    @property
    def MontoItemOtrMnda(self) -> float:
        return round(self._valor, 4)

    @MontoItemOtrMnda.setter
    def MontoItemOtrMnda(self, value: float):
        self._valor = value

    def __init__(self):
        self.PrcOtrMon = 0.0
        self.Moneda = ''
        self.FctConv = 0.0
        self.DctoOtrMnda = 0.0
        self.RecargoOtrMnda = 0.0
        self.MontoItemOtrMnda = 0.0