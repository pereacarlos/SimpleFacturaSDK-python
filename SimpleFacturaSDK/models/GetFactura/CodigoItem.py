from dataclasses import dataclass

@dataclass
class CodigoItem:
    __tipoCodigo: str = ''
    __valorCodigo: str = ''

    @property
    def TpoCodigo(self) -> str:
        return self.__tipoCodigo

    @TpoCodigo.setter
    def TpoCodigo(self, value: str):
        self.__tipoCodigo = value[:10] 

    @property
    def VlrCodigo(self) -> str:
        return self.__valorCodigo

    @VlrCodigo.setter
    def VlrCodigo(self, value: str):
        self.__valorCodigo = value[:35] 

    def __init__(self, TpoCodigo: str = '', VlrCodigo: str = ''):
        self.TpoCodigo = TpoCodigo
        self.VlrCodigo = VlrCodigo

    def to_dict(self):
        return {
            "TpoCodigo": self.TpoCodigo,
            "VlrCodigo": self.VlrCodigo
        }