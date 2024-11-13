class FoliosAnulablesEnt:
    def __init__(self, desde: int, hasta: int):
        self.desde = desde
        self.hasta = hasta

    @property
    def cantidad(self):
        return self.hasta - self.desde + 1


'''
from dataclasses import dataclass

@dataclass
class FoliosAnulablesEnt:
    desde: int
    hasta: int

    @property
    def cantidad(self) -> int:
        return self.hasta - self.desde + 1
        '''