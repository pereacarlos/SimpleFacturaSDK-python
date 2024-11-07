from dataclasses import dataclass

@dataclass
class Retenedor:
    IndAgente: str = ''
    MntBaseFaena: int = 0
    MntMargComer: int = 0
    PrcConsFinal: int = 0

    def __init__(self):
        self.IndAgente = ''
        self.MntBaseFaena = 0
        self.MntMargComer = 0
        self.PrcConsFinal = 0