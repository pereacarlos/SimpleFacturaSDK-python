from enum import Enum
import json

class TipoMonedaEnum(Enum):
    NotSet = ""
    Bolivar = "BOLIVAR"
    Boliviano = "BOLIVIANO"
    Chelin = "CHELIN"
    CoronaDin = "CORONA DIN"
    CoronaNor = "CORONA NOR"
    CoronaSC = "CORONA SC"
    CruzeiroReal = "CRUZEIRO REAL"
    DirHam = "DIRHAM"
    DolarAustraliano = "DOLAR AUST"
    DolarCan = "DOLAR CAN"
    DolarHK = "DOLAR HK"
    DolarNZ = "DOLAR NZ"
    DolarSin = "DOLAR SIN"
    DolarTai = "DOLAR TAI"
    DolarUsa = "DOLAR USA"
    Dracma = "DRACMA"
    Escudo = "ESCUDO"
    Euro = "EURO"
    Florin = "FLORIN"
    FrancoBel = "FRANCO BEL"
    FrancoFr = "FRANCO FR"
    FrancoSz = "FRANCO SZ"
    Guarani = "GUARANI"
    LibraEst = "LIBRA EST"
    Lira = "LIRA"
    MarcoAl = "MARCO AL"
    MarcoFin = "MARCO FIN"
    NuevoSol = "NUEVO SOL"
    OtrasMonedas = "OTRAS MONEDAS"
    Peseta = "PESETA"
    Peso = "PESO"
    PesoCl = "PESO CL"
    PesoCol = "PESO COL"
    PesoMex = "PESO MEX"
    PesoUrug = "PESO URUG"
    Rand = "RAND"
    Renminbi = "RENMINBI"
    Rupia = "RUPIA"
    Sucre = "SUCRE"
    Yen = "YEN"

    def description(self):
        descriptions = {
            "": "",
            "BOLIVAR": "BOLIVAR",
            "BOLIVIANO": "BOLIVIANO",
            "CHELIN": "CHELIN",
            "CORONA DIN": "CORONA DIN",
            "CORONA NOR": "CORONA NOR",
            "CORONA SC": "CORONA SC",
            "CRUZEIRO REAL": "CRUZEIRO REAL",
            "DIRHAM": "DIRHAM",
            "DOLAR AUST": "DOLAR AUST",
            "DOLAR CAN": "DOLAR CAN",
            "DOLAR HK": "DOLAR HK",
            "DOLAR NZ": "DOLAR NZ",
            "DOLAR SIN": "DOLAR SIN",
            "DOLAR TAI": "DOLAR TAI",
            "DOLAR USA": "DOLAR USA",
            "DRACMA": "DRACMA",
            "ESCUDO": "ESCUDO",
            "EURO": "EURO",
            "FLORIN": "FLORIN",
            "FRANCO BEL": "FRANCO BEL",
            "FRANCO FR": "FRANCO FR",
            "FRANCO SZ": "FRANCO SZ",
            "GUARANI": "GUARANI",
            "LIBRA EST": "LIBRA EST",
            "LIRA": "LIRA",
            "MARCO AL": "MARCO AL",
            "MARCO FIN": "MARCO FIN",
            "NUEVO SOL": "NUEVO SOL",
            "OTRAS MONEDAS": "OTRAS MONEDAS",
            "PESETA": "PESETA",
            "PESO": "PESO",
            "PESO CL": "PESO CL",
            "PESO COL": "PESO COL",
            "PESO MEX": "PESO MEX",
            "PESO URUG": "PESO URUG",
            "RAND": "RAND",
            "RENMINBI": "RENMINBI",
            "RUPIA": "RUPIA",
            "SUCRE": "SUCRE",
            "YEN": "YEN"
        }
        return descriptions.get(self.value, "")