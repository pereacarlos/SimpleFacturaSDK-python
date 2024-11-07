from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.CodigosAduana import TipoBultoEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class TipoBulto:
    CodTpoBultos: TipoBultoEnum = TipoBultoEnum.NotSet
    CantBultos: int = 0

    __marcas: str = field(default="", init=False)
    __idContainer: str = field(default="", init=False)
    __sello: str = field(default="", init=False)
    __emisorSello: str = field(default="", init=False)

    @property
    def Marcas(self) -> str:
        return self.__marcas

    @Marcas.setter
    def Marcas(self, value: str):
        self.__marcas = truncate(value, 255)

    @property
    def IdContainer(self) -> str:
        return self.__idContainer

    @IdContainer.setter
    def IdContainer(self, value: str):
        self.__idContainer = truncate(value, 25)

    @property
    def Sello(self) -> str:
        return self.__sello

    @Sello.setter
    def Sello(self, value: str):
        self.__sello = truncate(value, 20)

    @property
    def EmisorSello(self) -> str:
        return self.__emisorSello

    @EmisorSello.setter
    def EmisorSello(self, value: str):
        self.__emisorSello = truncate(value, 70)

    def __init__(self):
        self.CodTpoBultos = TipoBultoEnum.NotSet
        self.CantBultos = 0
        self.Marcas = ''
        self.IdContainer = ''
        self.Sello = ''
        self.EmisorSello = ''
