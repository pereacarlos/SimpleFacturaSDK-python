from enum import Enum


class TipoServicioEnum(Enum):
    NotSet = 0
    BoletaServiciosPeriodicos = 1
    BoletaServiciosPeriodicosDomiciliarios = 2
    BoletaVentasYServicios = 3
    BoletaEspectaculosPorTerceros = 4

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4"
        }
        return descriptions.get(self.value, "")
   
