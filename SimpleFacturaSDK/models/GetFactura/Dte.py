from dataclasses import dataclass, asdict
from SimpleFacturaSDK.models.GetFactura.DetalleDte import DetalleDte 
from SimpleFacturaSDK.models.GetFactura.DescuentosRecargos import DescuentosRecargos
from typing import Optional, List

@dataclass
class Dte:
    detalles: List[DetalleDte]
    referencias: List[dict]
    ambiente: str = ""
    folioReutilizado: str = ""
    importado: str  = ""
    codigoSii: int = 0
    tipoDte: str = ""
    estadoAcuse: str = ""
    fechaDte: str = ""
    fechaCreacion: str = ""
    folio: int = 0
    razonSocialReceptor: str = ""
    rutReceptor: str = ""
    trackId: int = 0
    neto: float = 0
    exento: float = 0
    iva: float = 0
    ivaTerceros: float = 0.0
    ivaPropio: float = 0.0
    total: float = 0.0
    totalImpuestosAdicionales: float = 0.0
    estadoSII: Optional[str] = None
    estado: Optional[str] = None
    fechaEmision: Optional[str] = None
    fechaRecepcionSII: Optional[str] = None
    razonSocialProveedor: Optional[str] = None
    rutProveedor: Optional[str] = None
    montoNoFacturable: Optional[float] = None
    formaPago: Optional[str] = None
    impuestos: Optional[List[dict]] = None

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
            estado=data.get('estado'),
            fechaDte=data.get('fechaDte'),
            fechaCreacion=data.get('fechaCreacion'),
            fechaEmision=data.get('fechaEmision'),
            fechaRecepcionSII=data.get('fechaRecepcionSII'),
            folio=data.get('folio'),
            razonSocialReceptor=data.get('razonSocialReceptor'),
            rutReceptor=data.get('rutReceptor'),
            razonSocialProveedor=data.get('razonSocialProveedor'),
            rutProveedor=data.get('rutProveedor'),
            trackId=data.get('trackId'),
            neto=data.get('neto'),
            exento=data.get('exento'),
            iva=data.get('iva'),
            ivaTerceros=data.get('ivaTerceros'),
            ivaPropio=data.get('ivaPropio'),
            totalImpuestosAdicionales=data.get('totalImpuestosAdicionales'),
            montoNoFacturable=data.get('montoNoFacturable'),
            formaPago=data.get('formaPago'),
            total=data.get('total'),
            detalles=detalles,
            referencias=data.get('referencias', []),
            impuestos=data.get('impuestos', []),
            
        )

    def to_dict(self):
        return asdict(self)
