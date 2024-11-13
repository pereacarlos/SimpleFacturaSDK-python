from dataclasses import dataclass

@dataclass
class FoliosAnulablesEnt:
    desde: int
    hasta: int

    @property
    def cantidad(self) -> int:
        return self.hasta - self.desde + 1
        ''