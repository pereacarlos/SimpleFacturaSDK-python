from dataclasses import dataclass, field

@dataclass
class OtraMonedaDetalle:
    PrcOtrMon: float = 0.0
    Moneda: str = ''
    FctConv: float = 0.0
    DctoOtrMnda: float = 0.0
    RecargoOtrMnda: float = 0.0
    MontoItemOtrMnda: float = 0.0

    __precioUnitario: float = field(default=0.0, metadata={"decimals": 4})
    __factorConversion: float = field(default=0.0, metadata={"decimals": 4})
    __descuento: float = field(default=0.0, metadata={"decimals": 4})
    __recargo: float = field(default=0.0, metadata={"decimals": 4})
    __valor: float = field(default=0.0, metadata={"decimals": 4})

    def __post_init__(self):
        self.__precioUnitario = round(self.PrcOtrMon, 4)
        self.__factorConversion = round(self.FctConv, 4)
        self.__descuento = round(self.DctoOtrMnda, 4)
        self.__recargo = round(self.RecargoOtrMnda, 4)
        self.__valor = round(self.MontoItemOtrMnda, 4)



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