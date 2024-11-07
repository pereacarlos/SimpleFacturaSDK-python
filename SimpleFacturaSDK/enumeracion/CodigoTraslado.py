from enum import Enum

class CodigoTrasladoEnum(Enum):
    NotSet = (0, "No Asignado")
    Exportador = (1, "Exportador")
    AgenteAduana = (2, "Agente de Aduana")
    Vendedor = (3, "Vendedor")
    ContribuyenteAutorizado = (4, "Contribuyente autorizado por el SII")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
