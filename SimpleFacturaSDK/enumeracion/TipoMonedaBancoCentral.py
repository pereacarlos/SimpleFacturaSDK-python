from enum import Enum

class TipoMonedaBancoCentralEnum(Enum):
    NotSet = ""
    NotSet2 = "000"
    BAHT_TAILANDES = 143
    BALBOA_PANAMENO = 161
    BOLIVAR_FUERTE = 134
    BOLIVIANO = 4
    COLON_COSTARRICENSE = 153
    CORONA_DANESA = 51
    CORONA_NORUEGA = 96
    CORONA_REP_CHECA = 146
    CORONA_SUECA = 113
    DINAR = 135
    DIRHAM = 139
    DOLAR_AUSTRALIANO = 36
    DOLAR_CANADIENSE = 6
    DOLAR_DE_BERMUDAS = 162
    DOLAR_DE_ESTADOS_UNIDOS = 13
    DOLAR_DE_LAS_ISLAS_CAIMAN = 163
    DOLAR_DE_NUEVA_ZELANDA = 97
    DOLAR_DE_SINGAPUR = 136
    DOLAR_FIYIANO = 154
    DOLAR_HONG_KONG = 127
    EURO = 142
    FORINT_HUNGRIA = 147
    FRANCO_POLINESICO = 156
    FRANCO_SUIZO = 82
    GUARANI = 23
    HRYVNIA_UCRANIANO = 164
    LIBRA_EGIPCIA = 165
    LIBRA_ESTERLINA = 102
    NUEVA_LIRA_TURCA = 149
    NUEVO_DOLAR_TAIWANES = 138
    NUEVO_SHEKEL_ISRAELI = 166
    NUEVO_SOL = 24
    PESO_ARGENTINO = 1
    PESO_CHILENO = 999
    PESO_COLOMBIANO = 129
    PESO_DOMINICANO = 167
    PESO_FILIPINO = 150
    PESO_MEXICANO = 132
    PESO_URUGUAYO = 26
    RAND = 128
    REAL = 5
    RINGGIT_MALASIA = 152
    RUBLO = 155
    RUPIA_INDIA = 137
    RUPIA_INDONESIA = 151
    TENGE_KAZAJSTAN = 169
    WON_DE_LA_REPUBLICA_DE_COREA_DEL_SUR = 144
    YEN = 72
    YUAN = 48
    ZLOTY_POLONIA = 145
    OTRAS_NO_ESPECIFICADAS = 900
    OTRAS_NO_ESPECIFICADAS2 = 200
    ONZA_TROY_ORO = 981
    ONZA_TROY_PLATA = 982
    PESO_ORO_SELLADO_CHILENO = 980
    DEG_DERECHO_ESPECIAL_DE_GIRO = 141
    BID_UNIDAD_DE_CUENTA = 2
    UF_UNIDAD_DE_FOMENTO = 998

    def __str__(self):
        descriptions = {
            "":"",
            "000": "000",
            143: "143",
            161: "161",
            134: "134",
            4: "4",
            153: "153",
            51: "51",
            96: "96",
            146: "146",
            113: "113",
            135: "135",
            139: "139",
            36: "36",
            6: "6",
            162: "162",
            13: "13",
            163: "163",
            97: "97",
            136: "136",
            154: "154",
            127: "127",
            142: "142",
            147: "147",
            156: "156",
            82: "82",
            23: "23",
            164: "164",
            165: "165",
            102: "102",
            149: "149",
            138: "138",
            166: "166",
            24: "24",
            1: "1",
            999: "999",
            129: "129",
            167: "167",
            150: "150",
            132: "132",
            26: "26",
            128: "128",
            5: "5",
            152: "152",
            155: "155",
            137: "137",
            151: "151",
            169: "169",
            144: "144",
            72: "72",
            48: "48",
            145: "145",
            900: "900",
            200: "200",
            981: "981",
            982: "982",
            980: "980",
            141: "141",
            2: "2",
            998: "998"
        }
        return descriptions.get(self, "Error")