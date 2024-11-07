from enum import Enum

class FormaPagoEnum(Enum):
    NotSet = (0, "No Asignado")
    Contado = (1, "Contado")
    Credito = (2, "Crédito")
    SinCosto = (3, "Sin Costo")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
