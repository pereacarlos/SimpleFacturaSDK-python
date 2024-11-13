from enum import Enum
import json

class ClaseCALEnum(Enum):
    NotSet = 0
    Contribuyente = 1
    Holding = 2
    EmpresaSoftware =3
    PrestadorServicioContable = 4

    def descripcion(self):
        Descripcion = {
            0: "",
            1: "Contribuyente. Sólo para su propio uso. Este CAL no se puede endosar",
            2: "Para uso de quien lo obtuvo y para empresas del holding. Este CAL es endosable",
            3: "Este CAL es endosable y vence anualmente",
            4: "Prestador de servicios contables"
        }
        return Descripcion.get(self.value, "")