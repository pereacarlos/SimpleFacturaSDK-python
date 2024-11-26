from enum import Enum
class TipoTrasladoEnum(Enum):
    NotSet = 0
    OperacionConstituyeVenta = 1
    VentaPorEfectuar = 2
    Consignaciones = 3
    EntregaGratuita = 4
    TrasladosInternos = 5
    OtrosTrasladosNoVenta = 6
    GuiaDeDevolucion = 7
    TrasladoParaExportacion = 8
    VentaParaExportacion = 9

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }
        return descriptions.get(self.value, "")