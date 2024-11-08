from enum import Enum

class ExpresionDineroEnum(Enum):
    NotSet = (0, "")
    PORCENTAJE = (1, "%")
    PESOS = (2, "$")

   
    @property
    def xml_enum(self):
        return self.value[1] 

    @property
    def description(self):
        return self.value[0]