from dataclasses import dataclass

@dataclass
class Comisiones:

    ValComNeto: int = 0 
    ValComExe: int = 0 
    ValComIVA: int = 0  

    def __init__(self, ValComNeto: int = 0, ValComExe: int = 0, ValComIVA: int = 0):
        self.ValComNeto = ValComNeto
        self.ValComExe = ValComExe
        self.ValComIVA = ValComIVA