from dataclasses import dataclass, field
from SimpleFacturaSDK.enumeracion.CodigosAduana import TipoBultoEnum

def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''

@dataclass
class TipoBulto:
    CodTpoBultos: TipoBultoEnum.NotSet
    CantBultos: int
    Marcas: str 
    IdContainer: str 
    Sello: str
    EmisorSello: str 

    __marcas: str 
    __idContainer: str
    __sello: str 
    __emisorSello: str

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