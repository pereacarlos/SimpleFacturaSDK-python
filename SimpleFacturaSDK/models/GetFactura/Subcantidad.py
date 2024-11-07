from dataclasses import dataclass

@dataclass
class SubCantidad:
    SubQty: float = 0.0
    __codigo: str = ''
    @property
    def SubCod(self) -> str:
        return self.__codigo

    @SubCod.setter
    def SubCod(self, value: str):
        self.__codigo = value[:35]

    def __init__(self):
        self.SubQty = 0.0
        self.SubCod = ''