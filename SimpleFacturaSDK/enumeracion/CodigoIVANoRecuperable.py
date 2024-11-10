from enum import Enum
import json

class CodigoIVANoRecuperableEnum(Enum):
    NotSet = (0, "")
    ComprasDestinadasAGenerarOperacioneExentas = (1, "Compras destinadas a generar operaciones no gravadas o exentas")
    FacturasRegistradasFueraPlazo = (2, "Facturas registradas fuera de plazo")
    GastosRechazados = (3, "Gastos rechazados")
    EntregaGratuita = (4, "Entrega gratuita")
    Otros = (9, "Otros")

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