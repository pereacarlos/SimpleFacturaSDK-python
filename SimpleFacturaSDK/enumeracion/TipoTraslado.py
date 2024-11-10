from enum import Enum
import json

class TipoTrasladoEnum(Enum):
    NotSet = (0, "No Asignado")
    OperacionConstituyeVenta = (1, "Operación Constituye Venta")
    VentaPorEfectuar = (2, "Venta Por Efectuar")
    Consignaciones = (3, "Consignaciones")
    EntregaGratuita = (4, "Entrega Gratuita")
    TrasladosInternos = (5, "Traslado Internos")
    OtrosTrasladosNoVenta = (6, "Otros Traslados No venta")
    GuiaDeDevolucion = (7, "Guia de Devolución")
    TrasladoParaExportacion = (8, "Traslado Para Exportación")
    VentaParaExportacion = (9, "Venta Para Exportación")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)