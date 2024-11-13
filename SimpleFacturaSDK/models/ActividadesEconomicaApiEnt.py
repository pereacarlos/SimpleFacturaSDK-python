from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class ActividadesEconomicaEnt:
    Codigo: int
    Descripcion: str = ""
    
'''
from dataclasses import dataclass

@dataclass
class ActividadeconomicaApiEnt:
    Codigo: int
    Descripcion: str = ""

    def __init__(self, Codigo: int, Descripcion: str = ""):
        self.Codigo = Codigo
        self.Descripcion = Descripcion'''