from dataclasses import dataclass

@dataclass
class CodigoItem:
    TpoCodigo: str
    VlrCodigo: str

    __tipoCodigo: str = ''
    __valorCodigo: str = ''

    #hacer el trucate de los valores
    def __post_init__(self):
        self.__tipoCodigo = self.TpoCodigo
        self.__valorCodigo = self.VlrCodigo


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TpoCodigo=data.get('TpoCodigo'),
            VlrCodigo=data.get('VlrCodigo')
        )
