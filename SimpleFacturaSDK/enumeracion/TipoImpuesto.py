from enum import Enum

class TipoImpuestoEnum(Enum):
    NotSet = (0, "No asignado")
    IVAMargenComercializacion = (14, "IVA Margen Comercialización")
    IVARetenidoTotal = (15, "IVA Retenido Total")
    IVARetenidoParcial = (16, "IVA Retenido Parcial")
    IVAAnticipadoFaenamientoCarne = (17, "IVA Anticipado Faenamiento Carne")
    IVAAnticipadoCarne = (18, "IVA Anticipado Carne")
    IVAAnticipadoHarina = (19, "IVA Anticipado Harina")
    ImpuestoAdicionalArticulo37_LetrasABC = (23, "Oro, Platino, Joyas y Pieles Finas")
    Licores = (24, "Licores y Destilados")
    Vinos = (25, "Vinos")
    Cervezas = (26, "Cervezas y Bebidas Alcohólicas")
    BebidasAnalcoholicasYMinerales = (27, "Bebidas Analcohólicas Y Minerales")
    BebidasAnalcoholicasYMineralesAltaAzucar = (271, "Bebidas Azucaradas")
    ImpuestoEspecificoDiesel = (28, "Impuesto Específico Diesel")
    IVARetenidoLegumbres = (30, "IVA retenido Legumbres")
    IVARetenidoSilvestres = (31, "IVA Retenido Silvestres")
    IVARetenidoGanado = (32, "IVA Retenido Ganado")
    IVARetenidoMadera = (33, "IVA Retenido Madera")
    IVARetenidoMaderaTotal = (331, "IVA Retenido Madera Total")
    IVARetenidoTrigo = (34, "IVA Retenido Trigo")
    ImpuestoEspecificoGasolina = (35, "IVA Específico Gasolina")
    IVARetenidoArroz = (36, "IVA Retenido Arroz")
    IVARetenidoHidrobiologicas = (37, "IVA Retenido Hidrobiologicas")
    IVARetenidoChatarra = (38, "IVA Retenido Chatarra")
    IVARetenidoPPA = (39, "IVA Retenido PPA")
    IVARetenidoConstruccion = (41, "IVA Retenido Construcción")
    ImpuestoAdicionalArticulo37_LetrasEHIL = (44, "Alfombras, Casas Rodantes, Caviar y Armas de Aire o Gas")
    ImpuestoAdicionalArticulo37_LetrasJ = (45, "Pirotecnia")
    IVARetenidoOro = (46, "IVA Retenido Oro")
    IVARetenidoCartones = (47, "IVA Retenido Cartones")
    IVARetenidoFrambuesas = (48, "IVA Retenido Frambuesas")
    FacturaCompraSinRetencion = (49, "Factura Compra Sin Retención")
    IVAMargenComercializacionInstrumentosPrepago = (50, "IVA Margen Comercialización Instrumentos Prepago")
    ImpuestoGasNaturalComprimido = (51, "Impuesto Gas Natural Comprimido")
    ImpuestoGasLicuado = (52, "Impuesto Gas Licuado")
    ImpuestoRetenidoSumplementeros = (53, "Impuesto Retenido Sumplementeros")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class TipoImpuestoResumido(Enum):
    NotSet = (0, "No asignado")
    Iva = (1, "IVA")
    Ley18211 = (2, "Ley 18.211")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
