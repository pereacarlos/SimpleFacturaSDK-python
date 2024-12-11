from enum import Enum
import json

class TipoImpuestoEnum(Enum):
    NotSet = 0
    IVAMargenComercializacion = 14
    IVARetenidoTotal = 15
    IVARetenidoParcial = 16
    IVAAnticipadoFaenamientoCarne = 17
    IVAAnticipadoCarne = 18
    IVAAnticipadoHarina = 19
    ImpuestoAdicionalArticulo37_LetrasABC = 23
    Licores = 24
    Vinos = 25
    Cervezas = 26
    BebidasAnalcoholicasYMinerales = 27
    BebidasAnalcoholicasYMineralesAltaAzucar = 271
    ImpuestoEspecificoDiesel = 28
    IVARetenidoLegumbres = 30
    IVARetenidoSilvestres = 31
    IVARetenidoGanado = 32
    IVARetenidoMadera = 33
    IVARetenidoMaderaTotal = 331
    IVARetenidoTrigo = 34
    ImpuestoEspecificoGasolina = 35
    IVARetenidoArroz = 36
    IVARetenidoHidrobiologicas = 37
    IVARetenidoChatarra = 38
    IVARetenidoPPA = 39
    IVARetenidoConstruccion = 41
    ImpuestoAdicionalArticulo37_LetrasEHIL = 44
    ImpuestoAdicionalArticulo37_LetrasJ = 45
    IVARetenidoOro = 46
    IVARetenidoCartones = 47
    IVARetenidoFrambuesas = 48
    FacturaCompraSinRetencion = 49
    IVAMargenComercializacionInstrumentosPrepago = 50
    ImpuestoGasNaturalComprimido = 51
    ImpuestoGasLicuado = 52
    ImpuestoRetenidoSumplementeros = 53

    def description(self):
        descriptions = {
            0: "",
            14: "14",
            15: "15",
            16: "16",
            17: "17",
            18: "18",
            19: "19",
            23: "23",
            24: "24",
            25: "25",
            26: "26",
            27: "27",
            271: "271",
            28: "28",
            30: "30",
            31: "31",
            32: "32",
            33: "33",
            331: "331",
            34: "34",
            35: "35",
            36: "36",
            37: "37",
            38: "38",
            39: "39",
            41: "41",
            44: "44",
            45: "45",
            46: "46",
            47: "47",
            48: "48",
            49: "49",
            50: "50",
            51: "51",
            52: "52",
            53: "53"

        }
        return description.get(self.value, "")
   

class TipoImpuestoResumido(Enum):
    NotSet = 0
    Iva = 1
    Ley18211 = 2

    def description(self):
        descriptions = {
            0: "",
            1: "1",
            2: "2"
        }
        return descriptions.get(self.value, "")