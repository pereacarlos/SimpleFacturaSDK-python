from enum import Enum

class TipoRecargoComisionEnum(Enum):
    NotSet = ("", "No Asignado")
    Comision = ("C", "Comisión")
    OtrosCargos = ("O", "Otros Cargos")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
