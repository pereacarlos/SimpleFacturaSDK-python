from enum import Enum

class TipoCuentaPagoEnum(Enum):
    NotSet = ("", "No Asignado")
    CuentaCorriente = ("CORRIENTE", "Cuenta Corriente")
    Ahorro = ("AHORRO", "Cuenta Ahorro")
    Vista = ("VISTA", "Cuenta Vista")
    Otro = ("", "Otro")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]