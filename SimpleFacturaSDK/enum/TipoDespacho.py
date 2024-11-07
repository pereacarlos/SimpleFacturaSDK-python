from enum import Enum

class TipoDespachoEnum(Enum):
    NotSet = (0, "No Asignado")
    Receptor = (1, "Receptor")
    EmisorACliente = (2, "Emisor A Cliente")
    EmisorAOtrasInstalaciones = (3, "Emisor A Otras Instalaciones")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]