from enum import Enum

class TipoTransCompra(Enum):
    DelGiro = (1, "1")
    SupermercadosYSimilares = (2, "2")
    AdquisicionOConstruccionDeBienesInmueblesBBRR = (3, "3")
    ActivoFijo = (4, "4")
    CompraIVAUsoComunONoRecuperable = (5, "5")
    Valor6 = (6, "6")
    Valor7 = (7, "7")

    @property
    def xml_enum(self):
        return self.value[1]

    @property
    def description(self):
        return self.value[0]

class TipoTransVenta(Enum):
    DelGiro = (1, "1")
    VentasQueNoSonDelGiroActivoFijoYOtros = (2, "2")
    VentaDeBienesInmueblesBBRR = (3, "3")
    NCEMR_SoloNCE = (4, "4")

    @property
    def xml_enum(self):
        return self.value[1] 

    @property
    def description(self):
        return self.value[0]