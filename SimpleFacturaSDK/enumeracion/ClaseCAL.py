from enum import Enum

class ClaseCALEnum(Enum):
    NotSet = (0, "")
    Contribuyente = (1, "Contribuyente. Sólo para su propio uso. Este CAL no se puede endosar")
    Holding = (2, "Para uso de quien lo obtuvo y para empresas del holding. Este CAL es endosable")
    EmpresaSoftware = (3, "Este CAL es endosable y vence anualmente")
    PrestadorServicioContable = (4, "Prestador de servicios contables")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
