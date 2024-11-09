from dataclasses import dataclass, field
def truncate(value: str, length: int) -> str:
    return value[:length] if value else ''
@dataclass
class SubCantidad:
    SubQty: float = 0.0
    SubCod: str = ''

    __codigo: str = field(default="", metadata={"max_length": 35})

    def __post_init__(self):
        self.__codigo = truncate(self.SubCod, 35)


    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            SubQty=data.get('SubQty'),
            SubCod=data.get('SubCod')
        )