from enum import Enum
import json

class IndicadorFacturacionExencionEnum(Enum):
    NotSet = (0, "Aún no se ha definido un valor.")
    NoAfectoOExento = (1, "No afecto o exento de IVA. No se usa este campo si la factura es exenta en forma global.")
    ProductoOServicioNoFacturable = (2, "Producto o servicio no es facturable.")
    GarantiaDeposito = (3, "Garantía de depósito por envases. (Cervezas, jugos, aguas minerales, bebidas analcohólicas u otros autorizados por resolución especial).")
    ItemNoVenta = (4, "Item no venta. Para facturas y guías de despacho (esta última con indicador de tipo de traslado de bienes = 1) y este item no será facturado.")
    ItemARebajar = (5, "Item a rebajar. Para guías de despacho NO VENTA que rebajan guía anterior. En el área de referencias se debe indicar la guía anterior.")
    ProductoOServicioNoFacturableNegativo = (6, "Producto o servicio no facturable negativo (excepto en liquidaciones-factura).")

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