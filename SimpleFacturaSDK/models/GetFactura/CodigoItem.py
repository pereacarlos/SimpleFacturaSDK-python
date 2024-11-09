from dataclasses import dataclass, field
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''
@dataclass
class CodigoItem:
    TpoCodigo: str = ''
    VlrCodigo: str = ''

    __tipoCodigo: str = field(default="" , metadata={"max_length": 10})
    __valorCodigo: str = field(default="" , metadata={"max_length": 35})

    #hacer el trucate de los valores
    def __post_init__(self):
        self.__tipoCodigo = truncate(self.TpoCodigo, 10)
        self.__valorCodigo = truncate(self.VlrCodigo, 35)


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            TpoCodigo=data.get('TpoCodigo'),
            VlrCodigo=data.get('VlrCodigo')
        )
