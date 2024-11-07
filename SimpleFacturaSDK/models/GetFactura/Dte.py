from dataclasses import dataclass, asdict
from typing import List, Optional
from models.GetFactura.DetalleDte import DetalleDte 
from models.GetFactura.ReferenciaDte import ReferenciaDte

@dataclass
class Dte:
    ambiente: str
    folioReutilizado: str
    folio: int
    importado: str
    codigoSii: int
    tipoDte: str
    estadoAcuse: str
    estadoSII: Optional[str]
    fechaDte: str
    fechaCreacion: str
    razonSocialReceptor: str
    rutReceptor: str
    trackId: int
    neto: float
    exento: float
    iva: float
    ivaTerceros: float
    ivaPropio: float
    totalImpuestosAdicionales: float
    total: float
    detalles: List[DetalleDte]
    referencias: List[dict]

    @classmethod
    def from_dict(cls, data: dict):
        detalles_data = data.get('detalles', [])
        detalles = [DetalleDte.from_dict(detalle) for detalle in detalles_data]

        return cls(
            ambiente=data.get('ambiente'),
            folioReutilizado=data.get('folioReutilizado'),
             importado=data.get('importado'),
            codigoSii=data.get('codigoSii'),
            tipoDte=data.get('tipoDte'),
            estadoAcuse=data.get('estadoAcuse'),
            estadoSII=data.get('estadoSII'),
            fechaDte=data.get('fechaDte'),
            fechaCreacion=data.get('fechaCreacion'),
            folio=data.get('folio'),
            razonSocialReceptor=data.get('razonSocialReceptor'),
            rutReceptor=data.get('rutReceptor'),
            trackId=data.get('trackId'),
            neto=data.get('neto'),
            exento=data.get('exento'),
            iva=data.get('iva'),
            ivaTerceros=data.get('ivaTerceros'),
            ivaPropio=data.get('ivaPropio'),
            totalImpuestosAdicionales=data.get('totalImpuestosAdicionales'),
            total=data.get('total'),
            detalles=detalles,
            referencias=data.get('referencias', [])
        )

    def to_dict(self):
        return asdict(self)
