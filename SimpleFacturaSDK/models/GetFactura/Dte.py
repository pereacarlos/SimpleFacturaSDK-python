from dataclasses import dataclass, asdict
from SimpleFacturaSDK.models.GetFactura.DetalleDte import DetalleDte 
from SimpleFacturaSDK.models.GetFactura.DescuentosRecargos import DescuentosRecargos
from typing import Optional, List

@dataclass
class Dte:
    ambiente: str
    folioReutilizado: str
    importado: str
    codigoSii: int
    tipoDte: str
    estadoAcuse: str
    estadoSII: Optional[str]
    estado: Optional[str]
    fechaDte: str
    fechaCreacion: str
    fechaEmision: Optional[str]
    fechaRecepcionSII: Optional[str]
    folio: int
    razonSocialReceptor: str
    rutReceptor: str
    razonSocialProveedor: Optional[str]
    rutProveedor: Optional[str]
    trackId: int
    neto: float
    exento: float
    iva: float
    ivaTerceros: float
    ivaPropio: float
    totalImpuestosAdicionales: float
    montoNoFacturable: Optional[float]
    formaPago: Optional[str]
    total: float
    detalles: List[DetalleDte]
    descuentosRecargos: List[DescuentosRecargos]
    referencias: List[dict]
    impuestos: List[dict]

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
            descuentosRecargos=DescuentosRecargos,
            referencias=data.get('referencias', []),
            impuestos=data.get('impuestos', []),
            
        )

    def to_dict(self):
        return asdict(self)
