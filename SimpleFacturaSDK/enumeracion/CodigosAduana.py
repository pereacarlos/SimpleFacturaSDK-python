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
    NotSet = (0, "No Asignado")
    MONTREAL = (111, "Montreal")
    COSTA_DEL_PACIFICO_1 = (112, "Costa del Pacífico 1")
    HALIFAX = (113, "Halifax")
    VANCOUVER = (114, "Vancouver")
    SAINT_JOHN = (115, "Saint John")
    TORONTO = (116, "Toronto")
    OTROS_PUERTOS_CANADA = (117, "Otros Puertos Canadá")
    BAYSIDE = (118, "Bayside")
    PORT_CARTIES = (120, "Puerto Cartier")
    COSTA_DEL_ATLANTICO = (121, "Costa del Atlántico")
    PUERTOS_DEL_GOLFO_ME = (122, "Puertos del Golfo México")
    COSTA_DEL_PACIFICO_2 = (123, "Costa del Pacífico 2")
    QUEBEC = (124, "Quebec")
    PRINCE_RUPERT = (125, "Prince Rupert")
    HAMILTON = (126, "Hamilton")
    BOSTON = (131, "Boston")
    NEW_HAVEN = (132, "New Haven")
    BRIDGEPORT = (133, "Bridgeport")
    NEW_YORK = (134, "Nueva York")
    FILADELFIA = (135, "Filadelfia")
    BALTIMORE = (136, "Baltimore")
    NORFOLK = (137, "Norfolk")
    CHARLESTON = (139, "Charlestón")
    SAVANAH = (140, "Savannah")
    MIAMI = (141, "Miami")
    EVERGLADES = (142, "Everglades")
    JACKSONVILLE = (143, "Jacksonville")
    PALM_BEACH = (145, "Palm Beach")
    BATON_ROUGE = (146, "Baton Rouge")
    COLUMBRES = (147, "Columbres")
    PITTSBURGH = (148, "Pittsburgh")
    DULUTH = (149, "Duluth")
    MILWAUKEE = (150, "Milwaukee")
    TAMPA = (151, "Tampa")
    PENSACOLA = (152, "Pensacola")
    MOBILE = (153, "Mobile")
    NEW_ORLEANS = (154, "Nueva Orleans")
    PORT_ARTHUR = (155, "Port Arthur")
    GALVESTON = (156, "Galveston")
    CORPUS_CRISTI = (157, "Corpus Cristi")
    BROWNSVILLE = (158, "Brownsville")
    HOUSTON = (159, "Houston")
    OAKLAND = (160, "Oakland")
    STOCKTON = (161, "Stockton")
    SEATTLE = (171, "Seattle")
    PORTLAND = (172, "Portland")
    SAN_FRANCISCO = (173, "San Francisco")
    LOS_ANGELES = (174, "Los Angeles")
    LONG_BEACH = (175, "Long Beach")
    SAN_DIEGO = (176, "San Diego")
    OTROS_PUERTOS_EE_UU_ = (180, "Otros Puertos EEUU")
    LOS_VILOS = (199, "Los Vilos")
    PATACHE = (204, "Patache")
    CALBUCO = (205, "Calbuco")
    MICHILLA = (206, "Michilla")
    PUERTO_ANGAMOS = (207, "Puerto Angamos")
    POSEIDON = (208, "Poseidon")
    TRES_PUENTES = (209, "Tres Puentes")
    OTROS_PUERTOS_MEXICO = (210, "Otros Puertos México")
    TAMPICO = (211, "Tampico")
    COSTA_DEL_PACIFICO_3 = (212, "Costa del Pacífico 3")
    VERACRUZ = (213, "Veracruz")
    COATZACOALCOS = (214, "Coatzacoalcos")
    GUAYMAS = (215, "Guaymas")
    MAZATLAN = (216, "Mazatlán")
    MANZANILLO = (217, "Manzanillo")
    ACAPULCO = (218, "Acapulco")
    GOLFO_DE_MEXICO_OTRO = (219, "Golfo de México, Otro")
    ALTAMIRA = (220, "Altamira")
    CRISTOBAL = (221, "Cristobal")
    BALBOA = (222, "Balboa")
    COLON = (223, "Colón")
    OTROS_PTOS__PANAMA = (224, "Otros Puertos Panamá")
    OTROS_PTOS__COLOMBIA = (231, "Otros Puertos Colombia")
    BUENAVENTURA = (232, "Buenaventura")
    BARRANQUILLA = (233, "Barranquilla")
    OTROS_PTOS__ECUADOR = (241, "Otros Puertos Ecuador")
    GUAYAQUIL = (242, "Guayaquil")
    OTROS_PTOS__DE_PERU = (251, "Otros Puertos Perú")
    CALLAO = (252, "Callao")
    ILO = (253, "Ilo")
    IQUITOS = (254, "Iquitos")
    OTROS_PTOS_ARGENTINA = (261, "Otros Puertos Argentina")
    BUENOS_AIRES = (262, "Buenos Aires")
    NECOCHEA = (263, "Necochea")
    MENDOZA = (264, "Mendoza")
    CORDOBA = (265, "Córdoba")
    BAHIA_BLANCA = (266, "Bahía Blanca")
    COMODORO_RIVADAVIA = (267, "Comodoro Rivadavia")
    PUERTO_MADRYN = (268, "Puerto Madryn")
    MAR_DEL_PLATA = (269, "Mar del Plata")
    ROSARIO = (270, "Rosario")
    OTROS_PTOS_URUGUAY = (271, "Otros Puertos Uruguay")
    MONTEVIDEO = (272, "Montevideo")
    OTROS_PTOS_VENEZUELA = (281, "Otros Puertos Venezuela")
    LA_GUAIRA = (282, "La Guaira")
    MARACAIBO = (285, "Maracaibo")
    OTROS_PTOS_BRASIL = (291, "Otros Puertos Brasil")
    SANTOS = (292, "Santos")
    RIO_DE_JANEIRO = (293, "Río de Janeiro")
    RIO_GRANDE_DEL_SUR = (294, "Río Grande del Sur")
    PARANAGUA = (295, "Paranaguá")
    SAO_PAULO = (296, "Sao Paulo")
    SALVADOR = (297, "Salvador")
    OTROS_ANT_HOLANDESA = (301, "Otros Ant Holandesa")
    CURAZAO = (302, "Curazao")
    OTROS_PTOS_AMERICA = (399, "Otros Puertos América")
    SHANGAI = (411, "Shanghái")
    DAIREN = (412, "Dairen")
    OTROS_PTOS_DE_CHINA = (413, "Otros Puertos China")
    OTROS_PUERT_COREA_N = (420, "Otros Puertos Corea del Norte")
    NAMPO = (421, "Nampo")
    BUSAN = (422, "Busan")
    OTROS_PTOS__COREA_S = (423, "Otros Puertos Corea del Sur")
    MANILA = (431, "Manila")
    OTROS_PTOS_FILIPINAS = (432, "Otros Puertos Filipinas")
    OTROS_PTOS_JAPONESES = (441, "Otros Puertos Japoneses")
    OSAKA = (442, "Osaka")
    KOBE = (443, "Kobe")
    YOKOHAMA = (444, "Yokohama")
    NAGOYA = (445, "Nagoya")
    SHIMIZUI = (446, "Shimizui")
    MOJI = (447, "Moji")
    YAWATA = (448, "Yawata")
    FUKUYAMA = (449, "Fukuyama")
    KAOHSIUNG = (451, "Kaohsiung")
    KEELUNG = (452, "Keelung")
    OTROS_PTOS_TAIWAN = (453, "Otros Puertos Taiwan")
    KARHG_ISLAND = (461, "Karhg Island")
    OTROS_PTO_IRAN_NO_ES = (462, "Otros Puertos Iran No Es")
    CALCUTA = (471, "Calcuta")
    OTROS_PTOS__DE_INDIA = (472, "Otros Puertos India")
    CHALNA = (481, "Chalna")
    OTROS_PTO_BANGLADESH = (482, "Otros Puertos Bangladesh")
    OTROS_PTO_SINGAPURE = (491, "Otros Puertos Singapure")
    HONG_KONG = (492, "Hong Kong")
    OTROS_PTO_ASIATICOS = (499, "Otros Puertos Asiaticos")
    CONSTANZA = (511, "Constanza")
    OTROS_PTO_DE_RUMANIA = (512, "Otros Puertos Rumanía")
    VARNA = (521, "Varna")
    OTROS_PTOS_BULGARIA = (522, "Otros Puertos Bulgaria")
    BELGRADO = (533, "Belgrado")
    OTROS_PUERTOS_DE_SER = (534, "Otros Puertos Ser")
    PODGORITSA = (535, "Podgoritsa")
    OTROS_PUERTOS_DE_MON = (536, "Otros Puertos de Mon")
    OTROS_PUERTOS_DE_CRO = (537, "Otros Puertos de Cro")
    RIJEKA = (538, "Rijeka")
    OTROS_PTOS_DE_ITALIA = (541, "Otros Puertos de Italia")
    GENOVA = (542, "Genova")
    LIORNA_LIVORNO = (543, "Liora, Livorno")
    NAPOLES = (544, "Napoles")
    SALERNO = (545, "Salermo")
    AUGUSTA = (546, "Augusta")
    SAVONA = (547, "Savona")
    OTROS_PTOS_FRANCIA = (551, "Otros Puertos de Francia")
    LA_PALLICE = (552, "La Pallice")
    LE_HAVRE = (553, "Le Havre")
    MARSELLA = (554, "Marsella")
    BURDEOS = (555, "Burdeos")
    CALAIS = (556, "Calais")
    BREST = (557, "Brest")
    RUAN = (558, "Ruan")
    OTROS_PTOS_ESPANA = (561, "Otros Puertos de España")
    CADIZ = (562, "Cadiz")
    BARCELONA = (563, "Barcelona")
    BILBAO = (564, "Bilbao")
    HUELVA = (565, "Huelva")
    SEVILLA = (566, "Sevilla")
    TARRAGONA = (567, "Tarragona")
    ALGECIRAS = (568, "Algeciras")
    VALENCIA = (569, "Valencia")
    LIVERPOOL = (571, "Liverpool")
    LONDRES = (572, "Londres")
    ROCHESTER = (573, "Rochester")
    ETEN_SALVERRY = (574, "Eten Salverry")
    OTROS_PTOS_INGLATERR = (576, "Otros Puertos de Inglaterra")
    DOVER = (577, "Dover")
    PLYMOUTH = (578, "Plymouth")
    HELSINKI = (581, "Helsinki")
    OTROS_PTOS_FINLANDIA = (582, "Otros Puertos de Finlandia")
    HANKO = (583, "Hanko")
    KEMI = (584, "Kemi")
    KOKKOLA = (585, "Kokkola")
    KOTKA = (586, "Kotra")
    OULO = (587, "Oulo")
    PIETARSAARI = (588, "Piertarsaari")
    PORI = (589, "Pori")
    BREMEN = (591, "Bremen")
    HAMBURGO = (592, "Hamburgo")
    NUREMBERG = (593, "Nuremberg")
    FRANKFURT = (594, "Frankfurt")
    DUSSELDORF = (595, "Dusseldorf")
    OTROS_PTOS_ALEMANIA = (596, "Otros Puertos de Alemania")
    CUXHAVEN = (597, "Cuxhaven")
    ROSTOCK = (598, "Rostock")
    OLDENBURG = (599, "Oldenburg")
    AMBERES = (601, "Amberes")
    OTROS_PTO_BELGICA = (602, "Otros Puertos de Belgica")
    ZEEBRUGGE = (603, "Zeebrugge")
    GHENT = (604, "Ghent")
    OOSTENDE = (605, "Oostende")
    LISBOA = (611, "Lisboa")
    OTROSS_PTOS_PORTUGAL = (612, "Otros Puertos de Portugal")
    SETUBAL = (613, "Setubal")
    AMSTERDAM = (621, "Amsterdam")
    ROTTERDAM = (622, "Rotterdam")
    OTROS_PTOS_HOLANDA = (623, "Otros Puertos de Holanda")
    GOTEMBURGO = (631, "Gotemburgo")
    OTROS_PTOS_SUECIA = (632, "Otros Puertos de Suecia")
    MALMO = (633, "Malmo")
    HELSIMBORG = (634, "Helsimborg")
    KALMAR = (635, "Kalmar")
    AARHUS = (641, "Aarhus")
    COPENHAGEN = (642, "Copenhagen")
    OTROS_PTOS_DINAMARCA = (643, "Otros Puertos de Dinamarca")
    AALBORG = (644, "Aalborg")
    ODENSE = (645, "Odense")
    OSLO = (651, "Oslo")
    OTROS_PTO__NORUEGA = (652, "Otros Puertos de Noruega")
    STAVANGER = (653, "Stavanger")
    OTROS_PTOS_EUROPA = (699, "Otros Puertos de Europa")
    DURBAM = (711, "Durbam")
    CIUDAD_DEL_CABO = (712, "Ciudad del Cabo")
    OTROS_PTO_SUDAFFRICA = (713, "Otros Puertos de Sudáfrica")
    SALDANHA = (714, "Saldanha")
    PORT_ELIZABETH = (715, "Puerto Elizabeth")
    MOSSEL_BAY = (716, "Mossel Bay")
    EAST_LONDON = (717, "East London")
    OTROS_PTO_DE_AFRICA = (799, "Otros Puertos de África")
    SIDNEY = (811, "Sidney")
    FREMANTLE = (812, "Fremantle")
    OTROS_PTOS_AUSTRALIA = (813, "Otros Puertos de Australia")
    ADELAIDA = (814, "Adelaida")
    DARWIN = (815, "Darwin")
    GERALDTON = (816, "Geraldton")
    OTROS_PTOS__OCEANIA = (899, "Otros Puertos de Oceanía")
    LUBRIC_ = (900, "Lubric")
    ARICA = (901, "Arica")
    IQUIQUE = (902, "Iquique")
    ANTOFAGASTA = (903, "Antofagasta")
    COQUIMBO = (904, "Coquimbo")
    VALPARAISO = (905, "Valparaíso")
    SAN_ANTONIO = (906, "San Antonio")
    TALCAHUANO = (907, "Talcahuano")
    SAN_VICENTE = (908, "San Vicente")
    LIRQUEN = (909, "Lirquen")
    PUERTO_MONTT = (910, "Puerto Montt")
    CHACABUCO_PTO_AYSEN = (911, "Chacabuco Puerto Aysen")
    PUNTA_ARENAS = (912, "Punta Arenas")
    PATILLOS = (913, "Patillos")
    TOCOPILLA = (914, "Tocopilla")
    MEJILLONES = (915, "Mejillones")
    TALTAL = (916, "Taltal")
    CHANARAL_BARQUITO = (917, "Barquito de Chañaral")
    CALDERA = (918, "Caldera")
    CALDERILLA = (919, "Calderilla")
    HUASCO_GUACOLDA = (920, "Huasco Guacolda")
    QUINTERO = (921, "Quintero")
    JUAN_FERNANDEZ = (922, "Juan Fernandez")
    CONSTUTUCION = (923, "Constitución")
    TOME = (924, "Tomé")
    PENCO = (925, "Penco")
    CORONEL = (926, "Coronel")
    LOTA = (927, "Lota")
    LEBU = (928, "Lebu")
    ISLA_DE_PASCUA = (929, "Isla de Pascua")
    CORRAL = (930, "Corral")
    ANCUD = (931, "Ancud")
    CASTRO = (932, "Castro")
    QUELLON = (933, "Quellón")
    CHAITEN = (934, "Chaiten")
    TORTEL = (935, "Tortel")
    NATALES = (936, "Natales")
    GUARELLO = (937, "Guarello")
    PUERTO_ANDINO = (938, "Puerto Andino")
    PERCY = (939, "Percy")
    CLARENCIA = (940, "Clarencia")
    GREGORIO = (941, "Gregorio")
    CABO_NEGRO = (942, "Cabo Negro")
    PUERTO_WILLIAMS = (943, "Puerto Williams")
    TER_ANTARTICO_CHILEN = (944, "Territorio Chileno Antártico")
    AEROP__CARRIEL_SUR = (945, "Aeropuerto Carriel Sur")
    GUAYACAN = (946, "Guayacan")
    PASO_PEHUENCHE = (947, "Paso Pehuenche")
    VENTANAS = (948, "Ventanas")
    PINO_HACHADO = (949, "Pino Hachado")
    CALETA_COLOSO = (950, "Caleta Coloso")
    AGUAS_NEGRAS = (951, "Aguas Negras")
    ZONA_FRANCA_IQUIQUE = (952, "Zona Franca de Iquique")
    ZONA_FRANCA_PTA_AREN = (953, "Zona Franca de Punta Arenas")
    RIO_MAYER = (954, "Río Mayer")
    RIO_MOSCO = (955, "Río Mosco")
    VISVIRI = (956, "Visviri")
    CHACALLUTA = (957, "Chacalluta")
    CHUNGARA = (958, "Chungara")
    COLCHANE = (959, "Colchane")
    ABRA_DE_NAPA = (960, "Abra de Napa")
    OLLAGUE = (961, "Ollague")
    SAN_PEDRO_DE_ATACAMA = (962, "San Pedro de Atacama")
    SOCOMPA = (963, "Socompa")
    SAN_FRANCISCO_2 = (964, "San Francisco 2")
    LOS_LIBERTADORES = (965, "Los Libertadores")
    MAHUIL_MALAL = (966, "Mahuil Malal")
    CARDENAL_SAMORE = (967, "Cardenal Samore")
    PEREZ_ROSALES = (968, "Perez Rosales")
    FUTALEUFU = (969, "Futaleufu")
    PALENA_CARRENLEUFU = (970, "Palena Carrenleufu")
    PANGUIPULLI = (971, "Panguipulli")
    HUAHUM = (972, "Huahum")
    LAGO_VERDE = (973, "Lago Verde")
    APPELEG = (974, "Appeleg")
    PAMPA_ALTA = (975, "Pampa Alta")
    HUEMULES = (976, "Huemules")
    CHILE_CHICO = (977, "Chile Chico")
    BAKER = (978, "Baker")
    DOROTEA = (979, "Dorotea")
    CASAS_VIEJAS = (980, "Casas Viejas")
    MONTE_AYMOND = (981, "Monte Aymond")
    SAN_SEBASTIAN = (982, "San Sebastián")
    COYHAIQUE_ALTO = (983, "Coyhaique Alto")
    TRIANA = (984, "Triana")
    IBANEZ_PALAVICINI = (985, "Ibáñez Pallavicini")
    VILLA_OHIGGINS = (986, "Villa O'Higgins")
    AEROP_CHACALLUTA = (987, "Aeropuerto Internacional Chacalluta")
    AEROP_DIEGO_ARACENA = (988, "Aeropuerto Internacional General Diego Aracena Aguilar")
    AEROP_CERRO_MORENO = (989, "Aeropuerto Cerro Moreno")
    AEROP_EL_TEPUAL = (990, "Aeropuerto El Tepual")
    AEROP_C_I_DEL_CAMPO = (991, "Aeropuerto Presidente Carlos Ibáñez del Campo")
    AEROP_A_M_BENITEZ = (992, "Aeropuerto Arturo Merino Benítez")
    AEROD_LOA = (993, "Aeropuerto Loa")
    ARICA_TACNA = (994, "Arica, Tacna")
    ARICA_LA_PAZ = (995, "Arica, La Paz")
    OTROS_PTOS__CHILENOS = (997, "Otros Puertos Chilenos")
    PASO_JAMA = (998, "Paso Jama")
    
    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]






























