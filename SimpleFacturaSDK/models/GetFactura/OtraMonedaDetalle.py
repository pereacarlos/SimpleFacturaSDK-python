from dataclasses import dataclass

@dataclass
class OtraMonedaDetalle:
    __precioUnitario: float = 0.0
    Moneda: str = ''
    __factorConversion: float = 0.0
    __descuento: float = 0.0
    __recargo: float = 0.0
    __valor: float = 0.0

    @property
    def PrcOtrMon(self) -> float:
        return round(self.__precioUnitario, 4)

    @PrcOtrMon.setter
    def PrcOtrMon(self, value: float):
        self.__precioUnitario = value

    @property
    def FctConv(self) -> float:
        return round(self.__factorConversion, 4)

    @FctConv.setter
    def FctConv(self, value: float):
        self.__factorConversion = value

    @property
    def DctoOtrMnda(self) -> float:
        return round(self.__descuento, 4)

    @DctoOtrMnda.setter
    def DctoOtrMnda(self, value: float):
        self.__descuento = value

    @property
    def RecargoOtrMnda(self) -> float:
        return round(self.__recargo, 4)

    @RecargoOtrMnda.setter
    def RecargoOtrMnda(self, value: float):
        self.__recargo = value

    @property
    def MontoItemOtrMnda(self) -> float:
        return round(self.__valor, 4)

    @MontoItemOtrMnda.setter
    def MontoItemOtrMnda(self, value: float):
        self.__valor = value

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            PrcOtrMon=data.get('PrcOtrMon'),
            Moneda=data.get('Moneda'),
            FctConv=data.get('FctConv'),
            DctoOtrMnda=data.get('DctoOtrMnda'),
            RecargoOtrMnda=data.get('RecargoOtrMnda'),
            MontoItemOtrMnda=data.get('MontoItemOtrMnda')
        )