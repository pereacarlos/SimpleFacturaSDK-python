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
    NotSet = 0
    FacturaServiciosPeriodicosDomiciliarios = 1
    FacturaOtrosServiciosPeriódicos = 2
    FacturaServicios = 3

    def description(self):
        descriptions = {
            0: "",
            1: 1,
            2: 2,
            3: 3
        }
        return descriptions.get(self.value, "")