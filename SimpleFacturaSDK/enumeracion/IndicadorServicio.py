from enum import Enum
import json

class IndicadorServicioEnum(Enum):
    NotSet = (0, "No Asignado")
    FacturaServiciosPeriodicosDomiciliarios = (1, "Factura de servicios periódicos domiciliarios")
    FacturaOtrosServiciosPeriódicos = (2, "Factura de otros servicios periódicos")
    FacturaServicios = (3, "Factura de servicios")
    ServiciosHoteleria = (4, "Servicios de hotelería")
    ServicioTransporteTerrestreInternacional = (5, "Servicios de transporte terrestre internacional")
    BoletaServiciosPeriodicos = (1, "Boleta de servicios periódicos")
    BoletaServiciosPeriodicosDomiciliarios = (2, "Boleta de servicios periódicos domiciliarios")
    BoletaVentasYServicios = (3, "Boleta de ventas y servicios")
    BoletaEspectaculosPorTerceros = (4, "Boleta de espectáculos por terceros")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

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
