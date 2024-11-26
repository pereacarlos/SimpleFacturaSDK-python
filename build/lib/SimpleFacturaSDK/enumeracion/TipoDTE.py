from enum import Enum
import json


class DTEType(Enum):
    NotSet = 0
    Factura = 30
    FacturaExenta = 32
    FacturaElectronica = 33
    FacturaElectronicaExenta = 34
    FacturaCompraElectronica = 46
    FacturaExportacionElectronica = 110
    NotaCreditoExportacionElectronica = 112
    NotaDebitoExportacionElectronica = 111
    GuiaDespachoElectronica = 52
    NotaDebitoElectronica = 56
    NotaCredito = 60
    NotaCreditoElectronica = 61
    BoletaElectronica = 39
    BoletaElectronicaExenta = 41

    def description(self):
        descriptions = {
            0: "NotSet",
            30: "Factura",
            32: "Factura Exenta",
            33: "Factura Electrónica",
            34: "Factura Electrónica Exenta",
            46: "Factura Compra Electrónica",
            110: "Factura Exportación Electrónica",
            112: "Nota Crédito Exportación Electrónica",
            111: "Nota Débito Exportación Electrónica",
            52: "Guía Despacho Electrónica",
            56: "Nota Débito Electrónica",
            60: "Nota Crédito",
            61: "Nota Crédito Electrónica",
            39: "Boleta Electrónica",
            41: "Boleta Electrónica Exenta"
        }
        return descriptions.get(self.value, "Error")



class DOCType(Enum):
    NotSet = 0
    FacturaElectronica = 33
    FacturaElectronicaExenta = 34
    FacturaCompraElectronica = 46
    GuiaDespachoElectronica = 52
    NotaDebitoElectronica = 56
    NotaCreditoElectronica = 61

    def description(self):
        descriptions = {
            0: "",
            33: "33",
            34: "34",
            46: "46",
            52: "52",
            56: "56",
            61: "61"
        }
        return descriptions.get(self.value, "Error")

class DTEFacturasType(Enum):
    NotSet = 0
    FacturaElectronica = 33
    FacturaElectronicaExcenta = 34
    FacturaCompraElectronica = 46
    LiquidacionFacturaElectronica = 43

    def description(self):
        descriptions = {
            0: "",
            33: "33",
            34: "34",
            46: "46",
            43: "43"
        }
        return descriptions.get(self.value, "Error")

class TipoDocumentoLibro(Enum):
    NotSet = ""
    FacturaManual = 30
    FacturaExentaManual = 32
    FacturaElectronica = 33
    FacturaExentaElectronica = 34
    BoletaVentasServicios = 36
    BoletaExenta = 38
    BoletaElectronica = 39
    LiquidacionFacturaManual = 40
    BoletaExentaElectronica = 41
    LiquidacionFacturaElectronica = 43
    FacturaCompra = 45
    FacturaCompraElectronica = 46
    NotaDebito = 55
    NotaDebitoElectronica = 56
    NotaCredito = 60
    NotaCreditoElectronica = 61
    FacturaExportacion = 101
    FacturaVentaExentaAZonaFrancaPrimaria = 102
    Liquidacion = 103
    NotaDebitoExportacion = 104
    BoletaLiquidacion = 105
    NotaCreditoExportacion = 106
    SRF = 108
    FacturaTurista = 109
    LiquidacionRecibidaPorMandante = 900
    FacturaVentaaEmpresasTerritorioPreferencial = 901
    ConocimientoEmbarque = 902
    DUS = 903
    ZonaFranca_FacturaTraspaso = 904
    FacturaReexpedicion = 905
    BoletaVentaModuloZonaFranca = 906
    FacturaVentaModuloZonaFranca = 907
    ZonaFranca_FacturaVentaModuloZF = 909
    ZonaFranca_SolicitudTrasladoZF = 910
    DeclaracionIngresoZonaFrancaPrimaria = 911
    DIN = 914
    DeclaracionIngresoZonaFranca = 918
    ResumenVentasNacionalesPasajesSinFactura = 919
    OtroRegistroAumentaDebito = 920
    LiquidacionRecibidaMandatario = 921
    OtrosRegistrosDisminuyeDebito = 922
    FacturaExportacionElectronica = 110
    NotaDebitoExportacionElectronica = 111
    NotaCreditoExportacionElectronica = 112
    ResumenVentasInternacionalPasajesSinFactura = 924
    AjusteAumentoTipoCambio = 500
    AjusteDisminucionTipoCambio = 501

    def description(self):
        descriptions = {
            "": "",
            30: "30",
            32: "32",
            33: "33",
            34: "34",
            36: "35",
            38: "38",
            39: "39",
            40: "40",
            41: "41",
            43: "43",
            45: "45",
            46: "46",
            55: "55",
            56: "56",
            60: "60",
            61: "61",
            101: "101",
            102: "102",
            103: "103",
            104: "104",
            105: "105",
            106: "106",
            108: "108",
            109: "109",
            900: "900",
            901: "901",
            902: "902",
            903: "903",
            904: "904",
            905: "905",
            906: "906",
            907: "907",
            909: "909",
            910: "910",
            911: "911",
            914: "914",
            918: "918",
            919: "919",
            920: "920",
            921: "921",
            922: "922",
            110: "110",
            111: "111",
            112: "112",
            924: "924",
            500: "500",
            501: "501"
        }
        return descriptions.get(self.value, "Error")
   