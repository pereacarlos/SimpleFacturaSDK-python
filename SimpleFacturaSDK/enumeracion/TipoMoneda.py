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

    @property
    def xml_enum(self):
        return self.value

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
