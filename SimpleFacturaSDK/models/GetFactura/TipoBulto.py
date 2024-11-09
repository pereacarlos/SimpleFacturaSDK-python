from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.CodigosAduana import TipoBultoEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class TipoBulto:
    CodTpoBultos: TipoBultoEnum = TipoBultoEnum.NotSet
    CantBultos: int = 0
    Marcas: str = ""
    IdContainer: str = ""
    Sello: str = ""
    EmisorSello: str = ""

    __marcas: str = field(default="", init=False, metadata={"max_length": 255})
    __idContainer: str = field(default="", init=False, metadata={"max_length": 25})
    __sello: str = field(default="", init=False, metadata={"max_length": 20})
    __emisorSello: str = field(default="", init=False, metadata={"max_length": 70})

    def __post_init__(self):
        self.__marcas = truncate(self.Marcas, 255)
        self.__idContainer = truncate(self.IdContainer, 25)
        self.__sello = truncate(self.Sello, 20)
        self.__emisorSello = truncate(self.EmisorSello, 70)

    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            CodTpoBultos=data.get('CodTpoBultos'),
            CantBultos=data.get('CantBultos'),
            Marcas=data.get('Marcas'),
            IdContainer=data.get('IdContainer'),
            Sello=data.get('Sello'),
            EmisorSello=data.get('EmisorSello')
        )