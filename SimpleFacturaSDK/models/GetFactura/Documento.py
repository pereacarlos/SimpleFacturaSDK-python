from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.SubTotal import SubTotal
from SimpleFacturaSDK.models.GetFactura.DescuentosRecargos import DescuentosRecargos
from SimpleFacturaSDK.models.GetFactura.Referencia import Referencia
from SimpleFacturaSDK.models.GetFactura.ComisionRecargo import ComisionRecargo

@dataclass
class Documento:
 
    Id: Optional[str] = None

    Encabezado: Optional[Encabezado] = field(default_factory=Encabezado)

    Detalle: List[Detalle] = field(default_factory=list)

    SubTotInfo: List[SubTotal] = field(default_factory=list)

    DscRcgGlobal: Optional[List[DescuentosRecargos]] = field(default_factory=list)

    Referencia: Optional[List[Referencia]] = field(default_factory=list)

   
    Comisiones: Optional[List[ComisionRecargo]] = field(default_factory=list)

    def __init__(self, Id: str = '', encabezado: Encabezado = None, Detalle: List[Detalle] = None, SubTotInfo: List[SubTotal] = None, DscRcgGlobal: List[DescuentosRecargos] = None, Referencia: List[Referencia] = None, Comisiones: List[ComisionRecargo] = None):
        self.Id = Id
        self.Encabezado = encabezado
        self.Detalle = Detalle
        self.SubTotInfo = SubTotInfo
        self.DscRcgGlobal = DscRcgGlobal
        self.Referencia = Referencia
        self.Comisiones = Comisiones

    def to_dict(self):
        return {
            "Id": self.Id,
            "Encabezado": self.Encabezado.to_dict() if self.Encabezado else None,
            "Detalle": [x.to_dict() for x in self.Detalle] if self.Detalle else None,
            "SubTotInfo": [x.to_dict() for x in self.SubTotInfo] if self.SubTotInfo else None,
            "DscRcgGlobal": [x.to_dict() for x in self.DscRcgGlobal] if self.DscRcgGlobal else None,
            "Referencia": [x.to_dict() for x in self.Referencia] if self.Referencia else None,
            "Comisiones": [x.to_dict() for x in self.Comisiones] if self.Comisiones else None
        }