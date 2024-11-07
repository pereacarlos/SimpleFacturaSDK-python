from dataclasses import dataclass

@dataclass
class Comisiones:

    val_com_neto: int = 0 
    val_com_exe: int = 0 
    val_com_iva: int = 0  

    def __init__(self, val_com_neto: int = 0, val_com_exe: int = 0, val_com_iva: int = 0):
        self.val_com_neto = val_com_neto
        self.val_com_exe = val_com_exe
        self.val_com_iva = val_com_iva