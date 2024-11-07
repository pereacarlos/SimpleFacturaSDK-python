from enum import Enum

class MedioPagoEnum(Enum):
    NotSet = ("", "No Asignado")
    CH = ("CH", "Cheque")
    CF = ("CF", "Cheque a fecha")
    LT = ("LT", "Letra")
    EF = ("EF", "Efectivo")
    PE = ("PE", "Pago a cuenta corriente")
    TC = ("TC", "Tarjeta de crédito")
    OT = ("OT", "Otro")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
