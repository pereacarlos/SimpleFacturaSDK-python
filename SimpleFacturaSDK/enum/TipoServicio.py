from enum import Enum

class TipoServicioEnum(Enum):
    NotSet = (0, "")
    BoletaServiciosPeriodicos = (1, "1")
    BoletaServiciosPeriodicosDomiciliarios = (2, "2")
    BoletaVentasYServicios = (3, "3")
    BoletaEspectaculosPorTerceros = (4, "4")

    @property
    def xml_enum(self):
        return self.value[1]
