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

    def __init__(self, Id: str = '', Encabezado: Encabezado = None, Detalle: List[Detalle] = None, SubTotInfo: List[SubTotal] = None, DscRcgGlobal: List[DescuentosRecargos] = None, Referencia: List[Referencia] = None, Comisiones: List[ComisionRecargo] = None):
        self.Id = Id
        self.Encabezado = Encabezado
        self.Detalle = Detalle
        self.SubTotInfo = SubTotInfo
        self.DscRcgGlobal = DscRcgGlobal
        self.Referencia = Referencia
        self.Comisiones = Comisiones

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            Id=data.get('id'),
            Encabezado=Encabezado.from_dict(data.get('Encabezado')) if data.get('Encabezado') else None,
            Detalle=[Detalle.from_dict(d) for d in data.get('Detalle', [])] if data.get('Detalle') else [],
            SubTotInfo=[SubTotal.from_dict(s) for s in data.get('SubTotInfo', [])] if data.get('SubTotInfo') else [],
            DscRcgGlobal=[DescuentosRecargos.from_dict(d) for d in data.get('DscRcgGlobal', [])] if data.get('DscRcgGlobal') else [],
            Referencia=[Referencia.from_dict(r) for r in data.get('Referencia', [])] if data.get('Referencia') else [],
            Comisiones=[ComisionRecargo.from_dict(c) for c in data.get('Comisiones', [])] if data.get('Comisiones') else []
        )

        