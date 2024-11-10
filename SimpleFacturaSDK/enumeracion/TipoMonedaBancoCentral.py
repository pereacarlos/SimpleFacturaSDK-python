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
            TipoMonedaBancoCentralEnum.NotSet: "Aún no se ha definido un valor.",
            TipoMonedaBancoCentralEnum.NotSet2: "NotSet2",
            TipoMonedaBancoCentralEnum.BAHT_TAILANDES: "BAHT TAILANDÉS",
            TipoMonedaBancoCentralEnum.BALBOA_PANAMENO: "BALBOA PANAMEÑO",
            TipoMonedaBancoCentralEnum.BOLIVAR_FUERTE: "BOLÍVAR FUERTE",
            TipoMonedaBancoCentralEnum.BOLIVIANO: "BOLIVIANO",
            TipoMonedaBancoCentralEnum.COLON_COSTARRICENSE: "COLÓN COSTARRICENSE",
            TipoMonedaBancoCentralEnum.CORONA_DANESA: "CORONA DANESA",
            TipoMonedaBancoCentralEnum.CORONA_NORUEGA: "CORONA NORUEGA",
            TipoMonedaBancoCentralEnum.CORONA_REP_CHECA: "CORONA REP. CHECA",
            TipoMonedaBancoCentralEnum.CORONA_SUECA: "CORONA SUECA",
            TipoMonedaBancoCentralEnum.DINAR: "DINAR",
            TipoMonedaBancoCentralEnum.DIRHAM: "DIRHAM",
            TipoMonedaBancoCentralEnum.DOLAR_AUSTRALIANO: "DÓLAR AUSTRALIANO",
            TipoMonedaBancoCentralEnum.DOLAR_CANADIENSE: "DÓLAR CANADIENSE",
            TipoMonedaBancoCentralEnum.DOLAR_DE_BERMUDAS: "DÓLAR DE BERMUDAS",
            TipoMonedaBancoCentralEnum.DOLAR_DE_ESTADOS_UNIDOS: "DÓLAR DE ESTADOS UNIDOS",
            TipoMonedaBancoCentralEnum.DOLAR_DE_LAS_ISLAS_CAIMAN: "DÓLAR DE LAS ISLAS CAIMÁN",
            TipoMonedaBancoCentralEnum.DOLAR_DE_NUEVA_ZELANDA: "DÓLAR DE NUEVA ZELANDA",
            TipoMonedaBancoCentralEnum.DOLAR_DE_SINGAPUR: "DÓLAR DE SINGAPUR",
            TipoMonedaBancoCentralEnum.DOLAR_FIYIANO: "DÓLAR FIYIANO",
            TipoMonedaBancoCentralEnum.DOLAR_HONG_KONG: "DÓLAR HONG KONG",
            TipoMonedaBancoCentralEnum.EURO: "EURO",
            TipoMonedaBancoCentralEnum.FORINT_HUNGRIA: "FORINT HUNGRÍA",
            TipoMonedaBancoCentralEnum.FRANCO_POLINESICO: "FRANCO POLINÉSICO",
            TipoMonedaBancoCentralEnum.FRANCO_SUIZO: "FRANCO SUIZO",
            TipoMonedaBancoCentralEnum.GUARANI: "GUARANÍ",
            TipoMonedaBancoCentralEnum.HRYVNIA_UCRANIANO: "HRYVNIA UCRANIANO",
            TipoMonedaBancoCentralEnum.LIBRA_EGIPCIA: "LIBRA EGIPCIA",
            TipoMonedaBancoCentralEnum.LIBRA_ESTERLINA: "LIBRA ESTERLINA",
            TipoMonedaBancoCentralEnum.NUEVA_LIRA_TURCA: "NUEVA LIRA TURCA",
            TipoMonedaBancoCentralEnum.NUEVO_DOLAR_TAIWANES: "NUEVO DÓLAR TAIWANÉS",
            TipoMonedaBancoCentralEnum.NUEVO_SHEKEL_ISRAELI: "NUEVO SHEKEL ISRAELÍ",
            TipoMonedaBancoCentralEnum.NUEVO_SOL: "NUEVO SOL",
            TipoMonedaBancoCentralEnum.PESO_ARGENTINO: "PESO ARGENTINO",
            TipoMonedaBancoCentralEnum.PESO_CHILENO: "PESO CHILENO",
            TipoMonedaBancoCentralEnum.PESO_COLOMBIANO: "PESO COLOMBIANO",
            TipoMonedaBancoCentralEnum.PESO_DOMINICANO: "PESO DOMINICANO",
            TipoMonedaBancoCentralEnum.PESO_FILIPINO: "PESO FILIPINO",
            TipoMonedaBancoCentralEnum.PESO_MEXICANO: "PESO MEXICANO",
            TipoMonedaBancoCentralEnum.PESO_URUGUAYO: "PESO URUGUAYO",
            TipoMonedaBancoCentralEnum.RAND: "RAND",
            TipoMonedaBancoCentralEnum.REAL: "REAL",
            TipoMonedaBancoCentralEnum.RINGGIT_MALASIA: "RINGGIT MALASIA",
            TipoMonedaBancoCentralEnum.RUBLO: "RUBLO",
            TipoMonedaBancoCentralEnum.RUPIA_INDIA: "RUPIA INDIA",
            TipoMonedaBancoCentralEnum.RUPIA_INDONESIA: "RUPIA INDONESIA",
            TipoMonedaBancoCentralEnum.TENGE_KAZAJSTAN: "TENGE KAZAJSTÁN",
            TipoMonedaBancoCentralEnum.WON_DE_LA_REPUBLICA_DE_COREA_DEL_SUR: "WON DE LA REPÚBLICA DE COREA DEL SUR",
            TipoMonedaBancoCentralEnum.YEN: "YEN",
            TipoMonedaBancoCentralEnum.YUAN: "YUAN",
            TipoMonedaBancoCentralEnum.ZLOTY_POLONIA: "ZLOTY POLONIA",
            TipoMonedaBancoCentralEnum.OTRAS_NO_ESPECIFICADAS: "OTRAS NO ESPECIFICADAS",
            TipoMonedaBancoCentralEnum.OTRAS_NO_ESPECIFICADAS2: "OTRAS NO ESPECIFICADAS2",
            TipoMonedaBancoCentralEnum.ONZA_TROY_ORO: "ONZA TROY ORO",
            TipoMonedaBancoCentralEnum.ONZA_TROY_PLATA: "ONZA TROY PLATA",
            TipoMonedaBancoCentralEnum.PESO_ORO_SELLADO_CHILENO: "PESO ORO SELLADO CHILENO",
            TipoMonedaBancoCentralEnum.DEG_DERECHO_ESPECIAL_DE_GIRO: "DEG DERECHO ESPECIAL DE GIRO",
            TipoMonedaBancoCentralEnum.BID_UNIDAD_DE_CUENTA: "BID UNIDAD DE CUENTA",
            TipoMonedaBancoCentralEnum.UF_UNIDAD_DE_FOMENTO: "UF UNIDAD DE FOMENTO"
        }
        return descriptions.get(self, "Unknown")

# Ejemplo de uso
print(TipoMonedaBancoCentralEnum.BAHT_TAILANDES)  # Salida: BAHT TAILANDÉS
print(TipoMonedaBancoCentralEnum.DOLAR_DE_ESTADOS_UNIDOS)  # Salida: DÓLAR DE ESTADOS UNIDOS