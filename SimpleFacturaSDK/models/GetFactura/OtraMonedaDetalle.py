from dataclasses import dataclass, field

@dataclass
class OtraMonedaDetalle:
    PrcOtrMon: float 
    Moneda: str 
    FctConv: float 
    DctoOtrMnda: float 
    RecargoOtrMnda: float 
    MontoItemOtrMnda: float

    __precioUnitario: float 
    __factorConversion: float 
    __descuento: float 
    __recargo: float 
    __valor: float 

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