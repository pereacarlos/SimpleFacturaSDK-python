from enum import Enum
import json

class IndicadorServicioEnum(Enum):
    NotSet = 0
    FacturaServiciosPeriodicosDomiciliarios = 1
    FacturaOtrosServiciosPeriódicos = 2
    FacturaServicios = 3
    ServiciosHoteleria = 4
    ServicioTransporteTerrestreInternacional = 5
    BoletaServiciosPeriodicos = 1
    BoletaServiciosPeriodicosDomiciliarios = 2
    BoletaVentasYServicios = 3
    BoletaEspectaculosPorTerceros = 4

    def description(self):
        descriptions = {
            0: "",
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            1: 1,
            2: 2,
            3: 3,
            4: 4
        }

    

class IndicadorServicioDetalleLibroEnum(Enum):
    NotSet = (0, "No Asignado")
    FacturaServiciosPeriodicosDomiciliarios = (1, "Factura de servicios periódicos domiciliarios")
    FacturaOtrosServiciosPeriódicos = (2, "Factura de otros servicios periódicos")
    FacturaServicios = (3, "Factura de servicios")

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
