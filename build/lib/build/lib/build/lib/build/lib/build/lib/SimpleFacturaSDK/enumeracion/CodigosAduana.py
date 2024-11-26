from enum import Enum

class FormaPagoExportacionEnum(Enum):
    NotSet = 0
    COB1 = 1
    ACRED = 11
    CBOF = 12
    COBRANZA =2 
    SINPAGO = 21
    ANTICIPO = 32
   
    def descripcion(self):
        description = {
            0: "",
            1: "1",
            11: "11",
            12: "12",
            2: "2",
            21: "21",
            32: "32",
            
        }
        return description.get(self.value, "")

class Moneda(Enum):
    NotSet = 0
    PESO = 1
    PESO_CHILENO = 200
    DOLAR_ESTADOUNIDENSE = 13
    BOLIVAR = 134
    BOLIVIANO = 4
    CHELIN = 37
    CORONA_DINAMARCA = 51
    CRUZEIRO_REAL = 5
    DIRHAM = 139
    DOLAR_AUSTRALIANO = 36
    DOLAR_CANADIENSE = 6
    EURO = 142
    FRANCO_BEL = 40
    FRANCO_FR = 58
    FRANCO_SZ = 82
    GUARANI = 23
    LIBRA_EST = 102
    LIRA = 71
    MARCO_AL = 30
    MARCO_FIN = 57
    NUEVO_SOL =24
    OTRAS_MONEDAS = 900
    PESETA = 53
    PESO_COL = 129
    PESO_MEX = 132
    PESO_URUG = 26
    RAND = 128
    RENMINBI = 48
    RUPIA = 137
    SUCRE = 130
    YEN = 72
    FLORIN = 64
    CORONA_NOR = 96
    DOLAR_NZ = 97
    CORONA_SC = 113
    DOLAR_HK = 127
    DRACMA = 131
    ESCUDO = 133
    DOLAR_SIN = 136
    DOLAR_TAI = 138

    def descripcion(self):
        description = {
            0: "No Asignado",
            1: "Peso",
            200: "Peso Chileno",
            13: "Dolar Estadounidense",
            134: "Bolivar",
            4: "Boliviano",
            37: "Chelin",
            51: "Corona Din",
            5: "Cruzeiro Real",
            139: "Dirham",
            36: "Dolar Australiano",
            6: "Dolar Canadiense",
            142: "Euro",
            40: "Franco Belga",
            58: "Franco Francés",
            82: "Franco Suizo",
            23: "Guarani",
            102: "Libra Esterlina",
            71: "Lira",
            30: "Marco Alemán",
            57: "Marco Finlandés",
            24: "Nuevo Sol",
            900: "Otras Monedas",
            53: "Peseta",
            129: "Peso Colombiano",
            132: "Peso Mexicano",
            26: "Peso Uruguayo",
            128: "Rand",
            48: "Renminbi",
            137: "Rupia",
            130: "Sucre",
            72: "Yen",
            64: "Florin",
            96: "Corona Noruega",
            97: "Dólar Neozeolandés",
            113: "Corona Sueca",
            127: "Dolar Hong Kong",
            131: "Dracma",
            133: "Escudo",
            136: "Dólar Singapur",
            138: "Dólar Tailandés"
        }
        return description.get(self.value, "")

class ModalidadVenta(Enum):
    NotSet = 0
    A_FIRME = 1
    BAJO_CONDICION = 2
    CONSIGNACION_LIBRE = 3
    CONSIGNACION_MINIMO_FIRME = 4
    SIN_PAGO = 9
   
    def descripcion(self):
        description = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            9: "9"
        }
        return description.get(self.value, "")

class ClausulaCompraVenta(Enum):
    NotSet = 0
    CIF = 1
    CFR = 2
    EXW = 3
    FAS = 4
    FOB = 5
    S_CLAUSULA = 6
    DDP = 9
    FCA = 10
    CPT = 11
    CIP = 12
    DAT = 17
    DAP = 18
    OTROS = 8

    def descripcion(self):
        description = {
            0: "",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            9: "9",
            7: "10",
            11: "11",
            12: "12",
            17: "17",
            18: "18",
            8: "8"
        }
        return description.get(self.value, "")

class ViasdeTransporte(Enum):
    NotSet = 0
    MARITIMA_FLUVIAL_Y_LACUSTRE = 1
    AEREO = 4
    POSTAL = 5
    FERROVIARIO = 6
    CARRETERO_O_TERRESTRE = 7
    ELEODUCTOS_GASODUCTOS = 8
    TENDIDO_ELECTRICO = 9
    OTRA = 10
    COURIER_AEREO = 11

    def descripcion(self):
        description = {
            0: "",
            1: "1",
            4: "4",
            5: "15",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "11"
        }
        return description.get(self.value, "")

class UnidadMedida(Enum):
    NotSet = 0
    SUM = 0
    TMB = 1
    U = 10
    DOC = 11
    U_JGO = 12
    MU = 13
    MT = 14
    MT2 = 15
    MCUB = 16
    PAR = 17
    KNFC = 18
    CARTON = 19
    QMB = 2
    KWH = 20
    BAR = 23
    M2_1MM = 24
    MKWH = 3
    TMN = 4
    KLT = 5
    KN = 6
    GN = 7
    HL = 8
    LT = 9

    def descripcion(self):
        description = {
            0: "",
            0: "0",
            1: "1",
            10: "10",
            11: "11",
            12: "12",
            13: "13",
            14: "14",
            15: "15",
            16: "16",
            17: "17",
            18: "18",
            19: "19",
            2: "2",
            20: "20",
            23: "23",
            24: "24",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }
        return description.get(self.value, "")
class TipoBultoEnum(Enum):
    NotSet = 0
    POLVO = 1
    PIEZA = 10
    TUBO = 11
    CILINDRO = 12
    ROLLO = 13
    BARRA = 16
    LINGOTE = 17
    TRONCO = 18
    BLOQUE = 19
    GRANOS = 2
    ROLLIZO = 20
    CAJON = 21
    CAJA_DE_CARTON = 22
    FARDO = 23
    BAUL = 24
    COFRE = 25
    ARMAZON = 26
    BANDEJA = 27
    CAJAMADERA = 28
    CAJALATA = 29
    NODULOS = 3
    BOTELLAGAS = 31
    BOTELLA = 32
    JAULA = 33
    BIDON = 34
    JABA = 35
    CESTA = 36
    BARRILETE = 37
    TONEL = 38
    PIPA = 39
    LIQUIDO = 4
    CAJANOESP = 40
    JARRO = 41
    FRASCO = 42
    DAMAJUANA = 43
    BARRIL = 44
    TAMBOR = 45
    CUNETE = 46
    TARRO = 47
    GAS = 5
    CUBO = 51
    PAQUETE = 61
    SACO = 62
    MALETA = 63
    BOLSA = 64
    BALA = 65
    RED = 66
    SOBRE = 67
    CONT20 = 73
    CONT40 = 74
    CONTENEDOR_REFRIGERADO = 75
    REEFER40 = 76
    ESTANQUE = 77
    CONTNOESP = 78
    PALLET = 80
    TABLERO = 81
    LAMINA = 82
    CARRETE = 83
    AUTOMOTOR = 85
    ATAUD = 86
    MAQUINARIA = 88
    PLANCHA = 89
    ATADO = 90
    BOBINA = 91
    BULTONOESP = 93
    SIN_BULTO = 98
    SIN_EMBALAR = 99

    def descripcion(self):
        description = {
            0: "0",
            1: "1",
            10: "10",
            11: "11",
            12: "12",
            13: "13",
            16: "16",
            17: "17",
            18: "18",
            19: "19",
            2: "2",
            20: "20",
            21: "21",
            22: "22",
            23: "23",
            24: "24",
            25: "25",
            26: "26",
            27: "27",
            28: "28",
            29: "29",
            3: "3",
            31: "31",
            32: "32",
            33: "33",
            34: "34",
            35: "35",
            36: "36",
            37: "37",
            38: "38",
            39: "39",
            4: "4",
            40: "40",
            41: "41",
            42: "42",
            43: "43",
            44: "44",
            45: "45",
            46: "46",
            47: "47",
            5: "5",
            51: "51",
            61: "61",
            62: "62",
            63: "63",
            64: "64",
            65: "65",
            66: "66",
            67: "67",
            73: "73",
            74: "74",
            75: "75",
            76: "76",
            77: "77",
            78: "78",
            80: "80",
            81: "81",
            82: "82",
            83: "83",
            85: "85",
            86: "86",
            88: "88",
            89: "89",
            90: "90",
            91: "91",
            93: "93",
            98: "98",
            99: "99"
        }
        return description.get(self.value, "")
  
class Paises(Enum):
    NotSet = 0
    SENEGAL = 101
    GAMBIA = 102
    GUINEA_BISSAU = 103
    GUINEA = 104
    SIERRA_LEONA = 105
    LIBERIA = 106
    COSTA_DE_MARFIL = 107
    GHANA = 108
    TOGO = 109
    NIGERIA = 111
    SUDAFRICA = 112
    BOTSWANA = 113
    LESOTHO = 114
    MALAWI = 115
    ZIMBABWE = 116
    ZAMBIA = 117
    COMORAS = 118
    MAURICIO = 119
    MADAGASCAR = 120
    MOZAMBIQUE = 121
    SWAZILANDIA = 122
    SUDAN = 123
    EGIPTO = 124
    LIBIA = 125
    TUNEZ = 126
    ARGELIA = 127
    MARRUECOS = 128
    CABO_VERDE = 129
    CHAD = 130
    NIGER = 131
    MALI = 133
    MAURITANIA = 134
    TANZANIA = 135
    UGANDA = 136
    KENIA = 137
    SOMALIA = 138
    ETIOPIA = 139
    ANGOLA = 140
    BURUNDI = 141
    RWANDA = 142
    REP_DEM_CONGO = 143
    CONGO = 144
    GABON = 145
    S_TOM_PRINCIPE = 146
    GUINEA_ECUATRL = 147
    REP_CENT_AFRIC = 148
    CAMERUN = 149
    BENIN = 150
    TERR_BRIT_EN_AF = 151
    TER_ESPAN_EN_AF = 152
    TERR_FRAN_EN_AF = 153
    DJIBOUTI = 155
    SEYCHELLES = 156
    NAMIBIA = 159
    SUDAN_DEL_SUR = 160
    BURKINA_FASO = 161
    ERITREA = 163
    ISLAS_MARSHALL = 164
    SAHARAUI = 165
    VENEZUELA = 201
    COLOMBIA = 202
    TRINID_Y_TOBAGO = 203
    BARBADOS = 204
    JAMAICA = 205
    REP_DOMINICANA = 206
    BAHAMAS = 207
    HAITI = 208
    CUBA = 209
    PANAMA = 210
    COSTA_RICA = 211
    NICARAGUA = 212
    EL_SALVADOR = 213
    HONDURAS = 214
    GUATEMALA = 215
    MEXICO = 216
    GUYANA = 217
    ECUADOR = 218
    PERU = 219
    BRASIL = 220
    BOLIVIA = 221
    PARAGUAY = 222
    URUGUAY = 223
    ARGENTINA = 224
    U_S_A = 225
    CANADA = 226
    TERR_BRIT_EN_AM = 227
    TERR_FRAN_EN_AM = 228
    TER_HOLAN_EN_AM = 229
    TERR_D_DINAMARC = 230
    DOMINICA = 231
    GRANADA = 232
    SANTA_LUCIA = 233
    S_VTE_Y_GRANAD = 234
    SURINAM = 235
    BELICE = 236
    ANTIGUA_Y_BBUDA = 240
    SNT_KIT_AND_NEVIS = 241
    ANGUILA = 242
    ARUBA = 243
    BERMUDAS = 244
    ISLAS_VIRG_BRIT = 245
    ISLAS_CAYMAN = 246
    ANTILLAS_NEERLA = 247
    TURCAS_Y_CAICOS = 248
    ISLAS_VIRG_EUA = 249
    MARTINICA = 250
    PUERTO_RICO = 251
    MONSERRAT = 252
    GROENLANDIA = 253
    JORDANIA = 301
    ARABIA_SAUDITA = 302
    KUWAIT = 303
    OMAN = 304
    CHIPRE = 305
    ISRAEL = 306
    IRAK = 307
    AFGHANISTAN = 308
    IRAN = 309
    SIRIA = 310
    LIBANO = 311
    QATAR = 312
    BAHREIN = 313
    SRI_LANKA = 314
    CAMBODIA = 315
    LAOS = 316
    INDIA = 317
    BUTAN = 318
    THAILANDIA = 319
    NEPAL = 320
    BANGLADESH = 321
    PALESTINA = 322
    PAKISTAN = 324
    VIETNAM = 325
    MYANMAR_EX_BIR = 326
    ISLAS_MALDIVAS = 327
    INDONESIA = 328
    MALASIA = 329
    TAIWAN_FORMOSA = 330
    JAPON = 331
    SINGAPUR = 332
    COREA_DEL_SUR = 333
    RPD_COREA_DEL_N = 334
    FILIPINAS = 335
    CHINA = 336
    MONGOLIA = 337
    EMIR_ARAB_UNID = 341
    HONG_KONG = 342
    TER_PORTUG_EAS = 343
    BRUNEI = 344
    MACAO = 345
    REPUBLICA_DE_YE = 346
    FIJI = 401
    NAURU = 402
    ISLAS_TONGA = 403
    SAMOA_OCC = 404
    NUEVA_ZELANDIA = 405
    AUSTRALIA = 406
    TERR_BRIT_EN_OP = 407
    TERR_FRAN_EN_OP = 408
    T_NORTEAM_EN_OP = 409
    PPUA_NVA_GUINEA = 412
    VANUATU = 415
    KIRIBATI = 416
    MICRONESIA = 417
    ISLAS_SALOMON = 418
    TUVALU = 419
    BELAU = 420
    NIUE = 421
    POLINESIA_FRAN = 422
    NUEVA_CALEDONIA = 423
    ISLAS_MARIANAS = 424
    GUAM = 425
    TIMOR_ORIENTAL = 426
    ISLAS_COOK = 427
    PORTUGAL = 501
    ITALIA = 504
    FRANCIA = 505
    IRLANDA = 506
    DINAMARCA = 507
    SUIZA = 508
    AUSTRIA = 509
    REINO_UNIDO = 510
    SUECIA = 511
    FINLANDIA = 512
    NORUEGA = 513
    BELGICA = 514
    HOLANDA = 515
    ISLANDIA = 516
    ESPANA = 517
    ALBANIA = 518
    RUMANIA = 519
    GRECIA = 520
    U_R_S_S = 521
    TURQUIA = 522
    MALTA = 523
    SANTA_SEDE = 524
    ANDORRA = 525
    BULGARIA = 527
    POLONIA = 528
    HUNGRIA = 530
    LUXEMBURGO = 532
    LIECHTENSTEIN = 534
    MONACO = 535
    SAN_MARINO = 536
    ARMENIA = 540
    AZERBAIJAN = 541
    BELARUS = 542
    BOSNIA_HEZGVINA = 543
    REPUBLICA_CHECA = 544
    REP_ESLOVACA = 545
    REPUBLICA_DE_SE = 546
    CROACIA = 547
    ESLOVENIA = 548
    ESTONIA = 549
    GEORGIA = 550
    KASAJSTAN = 551
    KIRGISTAN = 552
    LETONIA = 553
    LITUANIA = 554
    MACEDONIA = 555
    MOLDOVA = 556
    TADJIKISTAN = 557
    TURKMENISTAN = 558
    UCRANIA = 559
    UZBEKISTAN = 560
    MONTENEGRO = 561
    RUSIA = 562
    ALEMANIA = 563
    GIBRALTAR = 565
    GUERNSEY = 566
    ISLAS_DE_MAN = 567
    JERSEY = 568
    LOS_DEMAS = 888
    COMB_Y_LUBRIC = 901
    RANCHO_DE_NAVES = 902
    PESCA_EXTRA = 903
    ORIG_O_DEST_NO = 904
    ZF_IQUIQUE = 905
    DEPOSITO_FRANCO = 906
    ZF_PARENAS = 907
    ZF_ARICA_ZF_IND = 910
    CHILE = 997
    NAC_REPUTADA = 998
    OTROS = 999

    def descripcion(self):
        descriptions = {
            0: "",
            101: "101",
            102: "102",
            103: "103",
            104: "104",
            105: "105",
            106: "106",
            107: "107",
            108: "108",
            109: "109",
            111: "111",
            112: "112",
            113: "113",
            114: "114",
            115: "115",
            116: "116",
            117: "117",
            118: "118",
            119: "119",
            120: "120",
            121: "121",
            122: "122",
            123: "123",
            124: "124",
            125: "125",
            126: "126",
            127: "127",
            128: "128",
            129: "129",
            130: "130",
            131: "131",
            133: "133",
            134: "134",
            135: "135",
            136: "136",
            137: "137",
            138: "138",
            139: "139",
            140: "140",
            141: "141",
            142: "142",
            143: "143",
            144: "144",
            145: "145",
            146: "146",
            147: "147",
            148: "148",
            149: "149",
            150: "150",
            151: "151",
            152: "152",
            153: "153",
            155: "155",
            156: "156",
            159: "159",
            160: "160",
            161: "161",
            163: "163",
            164: "164",
            165: "165",
            201: "201",
            202: "202",
            203: "203",
            204: "204",
            205: "205",
            206: "206",
            207: "207",
            208: "208",
            209: "209",
            210: "210",
            211: "211",
            212: "212",
            213: "213",
            214: "214",
            215: "215",
            216: "216",
            217: "217",
            218: "218",
            219: "219",
            220: "220",
            221: "221",
            222: "222",
            223: "223",
            224: "224",
            225: "225",
            226: "226",
            227: "227",
            228: "228",
            229: "229",
            230: "230",
            231: "231",
            232: "232",
            233: "233",
            234: "234",
            235: "235",
            236: "236",
            240: "240",
            241: "241",
            242: "242",
            243: "243",
            244: "244",
            245: "245",
            246: "246",
            247: "247",
            248: "248",
            249: "249",
            250: "250",
            251: "251",
            252: "252",
            253: "253",
            301: "301",
            302: "302",
            303: "303",
            304: "304",
            305: "305",
            306: "306",
            307: "307",
            308: "308",
            309: "309",
            310: "310",
            311: "311",
            312: "312",
            313: "313",
            314: "314",
            315: "315",
            316: "316",
            317: "317",
            318: "318",
            319: "319",
            320: "320",
            321: "321",
            322: "322",
            324: "324",
            325: "325",
            326: "326",
            327: "327",
            328: "328",
            329: "329",
            330: "330",
            331: "331",
            332: "332",
            333: "333",
            334: "334",
            335: "335",
            336: "336",
            337: "337",
            341: "341",
            342: "342",
            343: "343",
            344: "344",
            345: "345",
            346: "346",
            401: "401",
            402: "402",
            403: "403",
            404: "404",
            405: "405",
            406: "406",
            407: "407",
            408: "408",
            409: "409",
            412: "412",
            415: "415",
            416: "416",
            417: "417",
            418: "418",
            419: "419",
            420: "420",
            421: "421",
            422: "422",
            423: "423",
            424: "424",
            425: "425",
            426: "426",
            427: "427",
            501: "501",
            504: "504",
            505: "505",
            506: "506",
            507: "507",
            508: "508",
            509: "509",
            510: "510",
            511: "511",
            512: "512",
            513: "513",
            514: "514",
            515: "515",
            516: "516",
            517: "517",
            518: "518",
            519: "519",
            520: "520",
            521: "521",
            522: "522",
            523: "523",
            524: "524",
            525: "525",
            527: "527",
            528: "528",
            530: "530",
            532: "532",
            534: "534",
            535: "535",
            536: "536",
            540: "540",
            541: "541",
            542: "542",
            543: "543",
            544: "544",
            545: "545",
            546: "546",
            547: "547",
            548: "548",
            549: "549",
            550: "550",
            551: "551",
            552: "552",
            553: "553",
            554: "554",
            555: "555",
            556: "556",
            557: "557",
            558: "558",
            559: "559",
            560: "560",
            561: "561",
            562: "562",
            563: "563",
            565: "565",
            566: "566",
            567: "567",
            568: "568",
            888: "888",
            901: "901",
            902: "902",
            903: "903",
            904: "904",
            905: "905",
            906: "906",
            907: "907",
            910: "910",
            997: "997",
            998: "998",
            999: "999"
        }
        return descriptions.get(self.value, "")


class Puertos(Enum):
    NotSet = 0
    MONTREAL = 111
    COSTA_DEL_PACIFICO_1 = 112
    HALIFAX = 113
    VANCOUVER = 114
    SAINT_JOHN = 115
    TORONTO = 116
    OTROS_PUERTOS_CANADA = 117
    BAYSIDE = 118
    PORT_CARTIES = 120
    COSTA_DEL_ATLANTICO = 121
    PUERTOS_DEL_GOLFO_ME = 122
    COSTA_DEL_PACIFICO_2 = 123
    QUEBEC = 124
    PRINCE_RUPERT = 125
    HAMILTON = 126
    BOSTON = 131
    NEW_HAVEN = 132
    BRIDGEPORT = 133
    NEW_YORK = 134
    FILADELFIA = 135
    BALTIMORE = 136
    NORFOLK = 137
    CHARLESTON = 139
    SAVANAH = 140
    MIAMI = 141
    EVERGLADES = 142
    JACKSONVILLE = 143
    PALM_BEACH = 145
    BATON_ROUGE = 146
    COLUMBRES = 147
    PITTSBURGH = 148
    DULUTH = 149
    MILWAUKEE = 150
    TAMPA = 151
    PENSACOLA = 152
    MOBILE = 153
    NEW_ORLEANS = 154
    PORT_ARTHUR = 155
    GALVESTON = 156
    CORPUS_CRISTI = 157
    BROWNSVILLE = 158
    HOUSTON = 159
    OAKLAND = 160
    STOCKTON = 161
    SEATTLE = 171
    PORTLAND = 172
    SAN_FRANCISCO = 173
    LOS_ANGELES = 174
    LONG_BEACH = 175
    SAN_DIEGO = 176
    OTROS_PUERTOS_EE_UU_ = 180
    LOS_VILOS = 199
    PATACHE = 204
    CALBUCO = 205
    MICHILLA = 206
    PUERTO_ANGAMOS = 207
    POSEIDON = 208
    TRES_PUENTES = 209
    OTROS_PUERTOS_MEXICO = 210
    TAMPICO = 211
    COSTA_DEL_PACIFICO_3 = 212
    VERACRUZ = 213
    COATZACOALCOS = 214
    GUAYMAS = 215
    MAZATLAN = 216
    MANZANILLO = 217
    ACAPULCO = 218
    GOLFO_DE_MEXICO_OTRO = 219
    ALTAMIRA = 220
    CRISTOBAL = 221
    BALBOA = 222
    COLON = 223
    OTROS_PTOS__PANAMA = 224
    OTROS_PTOS__COLOMBIA = 231
    BUENAVENTURA = 232
    BARRANQUILLA = 233
    OTROS_PTOS__ECUADOR =241
    GUAYAQUIL = 242
    OTROS_PTOS__DE_PERU = 251
    CALLAO = 252
    ILO = 253
    IQUITOS = 254
    OTROS_PTOS_ARGENTINA = 261
    BUENOS_AIRES = 262
    NECOCHEA = 263
    MENDOZA = 264
    CORDOBA = 265
    BAHIA_BLANCA = 266
    COMODORO_RIVADAVIA = 267
    PUERTO_MADRYN = 268
    MAR_DEL_PLATA = 269
    ROSARIO = 270
    OTROS_PTOS_URUGUAY = 271
    MONTEVIDEO = 272
    OTROS_PTOS_VENEZUELA = 281
    LA_GUAIRA = 282
    MARACAIBO = 285
    OTROS_PTOS_BRASIL = 291
    SANTOS = 292
    RIO_DE_JANEIRO = 293
    RIO_GRANDE_DEL_SUR = 294
    PARANAGUA = 295
    SAO_PAULO = 296
    SALVADOR = 297
    OTROS_ANT_HOLANDESA = 301
    CURAZAO = 302
    OTROS_PTOS_AMERICA = 399
    SHANGAI = 411
    DAIREN = 412
    OTROS_PTOS_DE_CHINA = 413
    OTROS_PUERT_COREA_N = 420
    NAMPO = 421
    BUSAN = 422
    OTROS_PTOS__COREA_S = 423
    MANILA = 431
    OTROS_PTOS_FILIPINAS = 432
    OTROS_PTOS_JAPONESES = 441
    OSAKA = 442
    KOBE = 443
    YOKOHAMA = 444
    NAGOYA = 445
    SHIMIZUI = 446
    MOJI = 447
    YAWATA = 448
    FUKUYAMA = 449
    KAOHSIUNG = 451
    KEELUNG = 452
    OTROS_PTOS_TAIWAN = 453
    KARHG_ISLAND = 461
    OTROS_PTO_IRAN_NO_ES = 462
    CALCUTA = 471
    OTROS_PTOS__DE_INDIA = 472
    CHALNA = 481
    OTROS_PTO_BANGLADESH =482
    OTROS_PTO_SINGAPURE = 491
    HONG_KONG = 492
    OTROS_PTO_ASIATICOS = 499
    CONSTANZA = 511
    OTROS_PTO_DE_RUMANIA = 512
    VARNA = 521
    OTROS_PTOS_BULGARIA = 522
    BELGRADO = 533
    OTROS_PUERTOS_DE_SER = 534
    PODGORITSA = 535
    OTROS_PUERTOS_DE_MON = 536
    OTROS_PUERTOS_DE_CRO = 537
    RIJEKA = 538
    OTROS_PTOS_DE_ITALIA = 541
    GENOVA = 542
    LIORNA_LIVORNO = 543
    NAPOLES = 544
    SALERNO = 545
    AUGUSTA = 546
    SAVONA = 547
    OTROS_PTOS_FRANCIA = 551
    LA_PALLICE = 552
    LE_HAVRE = 553
    MARSELLA = 554
    BURDEOS = 555
    CALAIS = 556
    BREST = 557
    RUAN = 558
    OTROS_PTOS_ESPANA = 561
    CADIZ = 562
    BARCELONA = 563
    BILBAO = 564
    HUELVA = 565
    SEVILLA = 566
    TARRAGONA = 567
    ALGECIRAS = 568
    VALENCIA = 569
    LIVERPOOL = 571
    LONDRES = 572
    ROCHESTER = 573
    ETEN_SALVERRY = 574
    OTROS_PTOS_INGLATERR = 576
    DOVER = 577
    PLYMOUTH = 578
    HELSINKI =581
    OTROS_PTOS_FINLANDIA = 582
    HANKO = 583
    KEMI = 584
    KOKKOLA = 585
    KOTKA = 586
    OULO = 587
    PIETARSAARI = 588
    PORI = 289
    BREMEN = 291
    HAMBURGO = 592
    NUREMBERG = 593
    FRANKFURT = 594
    DUSSELDORF = 595
    OTROS_PTOS_ALEMANIA = 596
    CUXHAVEN = 597
    ROSTOCK = 598
    OLDENBURG = 599
    AMBERES = 601
    OTROS_PTO_BELGICA = 602
    ZEEBRUGGE = 603
    GHENT = 604
    OOSTENDE = 605
    LISBOA = 611
    OTROSS_PTOS_PORTUGAL = 612
    SETUBAL = 613
    AMSTERDAM = 621
    ROTTERDAM = 622
    OTROS_PTOS_HOLANDA = 623
    GOTEMBURGO = 631
    OTROS_PTOS_SUECIA = 632
    MALMO = 633
    HELSIMBORG = 634
    KALMAR = 635
    AARHUS = 641
    COPENHAGEN = 642
    OTROS_PTOS_DINAMARCA = 643
    AALBORG = 644
    ODENSE = 645
    OSLO = 651
    OTROS_PTO__NORUEGA = 652
    STAVANGER = 653
    OTROS_PTOS_EUROPA = 699
    DURBAM = 711
    CIUDAD_DEL_CABO = 712
    OTROS_PTO_SUDAFFRICA = 713
    SALDANHA = 714
    PORT_ELIZABETH = 715
    MOSSEL_BAY = 716
    EAST_LONDON = 717
    OTROS_PTO_DE_AFRICA = 799
    SIDNEY = 811
    FREMANTLE = 812
    OTROS_PTOS_AUSTRALIA = 813
    ADELAIDA = 814
    DARWIN = 815
    GERALDTON = 816
    OTROS_PTOS__OCEANIA = 899
    LUBRIC_ = 900
    ARICA = 901
    IQUIQUE = 902
    ANTOFAGASTA = 903
    COQUIMBO = 904
    VALPARAISO = 905
    SAN_ANTONIO = 906
    TALCAHUANO = 907
    SAN_VICENTE = 908
    LIRQUEN = 909
    PUERTO_MONTT = 910
    CHACABUCO_PTO_AYSEN = 911
    PUNTA_ARENAS = 912
    PATILLOS = 913
    TOCOPILLA = 914
    MEJILLONES = 915
    TALTAL = 916
    CHANARAL_BARQUITO = 917
    CALDERA = 918
    CALDERILLA = 919
    HUASCO_GUACOLDA = 920
    QUINTERO = 921
    JUAN_FERNANDEZ = 922
    CONSTUTUCION = 923
    TOME = 924
    PENCO = 925
    CORONEL = 926
    LOTA = 927
    LEBU = 928
    ISLA_DE_PASCUA = 929
    CORRAL = 930
    ANCUD = 931
    CASTRO = 932
    QUELLON = 933
    CHAITEN = 934
    TORTEL = 935
    NATALES = 936
    GUARELLO = 937
    PUERTO_ANDINO = 938
    PERCY = 939
    CLARENCIA =940
    GREGORIO = 941
    CABO_NEGRO = 942
    PUERTO_WILLIAMS = 943
    TER_ANTARTICO_CHILEN = 944
    AEROP__CARRIEL_SUR = 945
    GUAYACAN = 946
    PASO_PEHUENCHE = 947
    VENTANAS = 948
    PINO_HACHADO = 949
    CALETA_COLOSO = 950
    AGUAS_NEGRAS = 951
    ZONA_FRANCA_IQUIQUE = 952
    ZONA_FRANCA_PTA_AREN = 953
    RIO_MAYER = 954
    RIO_MOSCO = 955
    VISVIRI = 956
    CHACALLUTA = 957
    CHUNGARA = 958
    COLCHANE = 959
    ABRA_DE_NAPA = 960
    OLLAGUE = 961
    SAN_PEDRO_DE_ATACAMA = 962
    SOCOMPA = 963
    SAN_FRANCISCO_2 = 964
    LOS_LIBERTADORES = 965
    MAHUIL_MALAL = 966
    CARDENAL_SAMORE = 967
    PEREZ_ROSALES = 968
    FUTALEUFU = 969
    PALENA_CARRENLEUFU = 970
    PANGUIPULLI = 971
    HUAHUM = 972
    LAGO_VERDE = 973
    APPELEG = 974
    PAMPA_ALTA = 975
    HUEMULES = 976
    CHILE_CHICO =977
    BAKER = 978
    DOROTEA = 979
    CASAS_VIEJAS = 980
    MONTE_AYMOND = 981
    SAN_SEBASTIAN = 982
    COYHAIQUE_ALTO = 983
    TRIANA = 984
    IBANEZ_PALAVICINI = 985
    VILLA_OHIGGINS = 986
    AEROP_CHACALLUTA = 987
    AEROP_DIEGO_ARACENA = 988
    AEROP_CERRO_MORENO =989
    AEROP_EL_TEPUAL = 990
    AEROP_C_I_DEL_CAMPO = 991
    AEROP_A_M_BENITEZ = 992
    AEROD_LOA = 993
    ARICA_TACNA = 994
    ARICA_LA_PAZ = 995
    OTROS_PTOS__CHILENOS = 997
    PASO_JAMA = 998
    
    def description(self):
        descriptions = {
            0: "",
            111: "111",
            112: "112",
            113: "113",
            114: "114",
            115: "115",
            116: "116",
            117: "117", 
            118: "118",
            120: "120",
            121: "121",
            122: "122",
            123: "123",
            124: "124",
            125: "125",
            126: "126",
            131: "131",
            132: "132",
            133: "133",
            134: "134",
            135: "135",
            136: "136",
            137: "137",
            139: "139",
            140: "140",
            141: "141",
            142: "142",
            143: "143",
            145: "145",
            146: "146",
            147: "147",
            148: "148",
            149: "149",
            150: "150",
            151: "151",
            152: "152",
            153: "153",
            154: "154",
            155: "155",
            156: "156",
            157: "157",
            158: "158",
            159: "159",
            160: "160",
            161: "161",
            171: "171",
            172: "172",
            173: "173",
            174: "174",
            175: "175",
            176: "176",
            180: "180",
            199: "199",
            204: "204",
            205: "205",
            206: "206",
            207: "207",
            208: "208",
            209: "209",
            210: "210",
            211: "211",
            212: "212",
            213: "213",
            214: "214",
            215: "215",
            216: "216",
            217: "217",
            218: "218",
            219: "219",
            220: "220",
            221: "221",
            222: "222",
            223: "223",
            224: "224",
            231: "231",
            232: "232",
            233: "233",
            241: "241",
            242: "242",
            251: "251",
            252: "252",
            253: "253",
            254: "254",
            261: "261",
            262: "262",
            263: "263",
            264: "264",
            265: "265",
            266: "266",
            267: "267",
            268: "268",
            269: "269",
            270: "270",
            271: "271",
            272: "272",
            281: "281",
            282: "282",
            285: "285",
            291: "291",
            292: "292",
            293: "293",
            294: "294",
            295: "295",
            296: "296",
            297: "297",
            301: "301",
            302: "302",
            399: "399",
            411: "411",
            412: "412",
            413: "413",
            420: "420",
            421: "421",
            422: "422",
            423: "423",
            431: "431",
            432: "432",
            441: "441",
            442: "442",
            443: "443",
            444: "444",
            445: "445",
            446: "446",
            447: "447",
            448: "448",
            449: "449",
            451: "451",
            452: "452",
            453: "453",
            461: "461",
            462: "462",
            471: "471",
            472: "472",
            481: "481",
            482: "482",
            491: "491",
            492: "492",
            499: "499",
            511: "511",
            512: "512",
            521: "521",
            522: "522",
            533: "533",
            534: "534",
            535: "535",
            536: "536",
            537: "537",
            538: "538",
            541: "541",
            542: "542",
            543: "543",
            544: "544",
            545: "545",
            546: "546",
            547: "547",
            551: "551",
            552: "552",
            553: "553",
            554: "554",
            555: "555",
            556: "556",
            557: "557",
            558: "558",
            561: "561",
            562: "562",
            563: "563",
            564: "564",
            565: "565",
            566: "566",
            567: "567",
            568: "568",
            569: "569",
            571: "571",
            572: "572",
            573: "573",
            574: "574",
            576: "576",
            577: "577",
            578: "578",
            581: "581",
            582: "582",
            583: "583",
            584: "584",
            585: "585",
            586: "586",
            587: "587",
            588: "588",
            589: "589",
            591: "591",
            592: "592",
            593: "593",
            594: "594",
            595: "595",
            596: "596",
            597: "597",
            598: "598",
            599: "599",
            601: "601",
            602: "602",
            603: "603",
            604: "604",
            605: "605",
            611: "611",
            612: "612",
            613: "613",
            621: "621",
            622: "622",
            623: "623",
            631: "631",
            632: "632",
            633: "633",
            634: "634",
            635: "635",
            641: "641",
            642: "642",
            643: "643",
            644: "644",
            645: "645",
            651: "651",
            652: "652",
            653: "653",
            699: "699",
            711: "711",
            712: "712",
            713: "713",
            714: "714",
            715: "715",
            716: "716",
            717: "717",
            799: "799",
            811: "811",
            812: "812",
            813: "813",
            814: "814",
            815: "815",
            816: "816",
            899: "899",
            900: "900",
            901: "901",
            902: "902",
            903: "903",
            904: "904",
            905: "905",
            906: "906",
            907: "907",
            908: "908",
            909: "909",
            910: "910",
            911: "911",
            912: "912",
            913: "913",
            914: "914",
            915: "915",
            916: "916", 
            917: "917",
            918: "918",
            919: "919",
            920: "920",
            921: "921",
            922: "922",
            923: "923",
            924: "924",
            925: "925",
            926: "926",
            927: "927",
            928: "928",
            929: "929",
            930: "930",
            931: "931",
            932: "932",
            933: "933",
            934: "934",
            935: "935",
            936: "936",
            937: "937",
            938: "938",
            939: "939",
            940: "940",
            941: "941",
            942: "942",
            943: "943",
            944: "944",
            945: "945",
            946: "946",
            947: "947",
            948: "948",
            949: "949",
            950: "950",
            951: "951",
            952: "952",
            953: "953",
            954: "954",
            955: "955",
            956: "956", 
            957: "957",
            958: "958",
            959: "959",
            960: "960",
            961: "961",
            962: "962",
            963: "963",
            964: "964",
            965: "965",
            966: "966",
            967: "967",
            968: "968",
            969: "969",
            970: "970",
            971: "971",
            972: "972",
            973: "973",
            974: "974",
            975: "975",
            976: "976",
            977: "977",
            978: "978",
            979: "979",
            980: "980",
            981: "981",
            982: "982",
            983: "983",
            984: "984",
            985: "985",
            986: "986",
            987: "987",
            988: "988",
            989: "989",
            990: "990",
            991: "991",
            992: "992",
            994: "994",
            995: "995",
            997: "997",
            998: "998"

        }
        return descriptions.get(self.value, "")































