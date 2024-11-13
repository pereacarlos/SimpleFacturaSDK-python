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
        return descriptions.get(self.value, "Unknown")



class DOCType(Enum):
    NotSet = (0, "No Asignado")
    FacturaElectronica = (33, "Factura Electrónica")
    FacturaElectronicaExenta = (34, "Factura Electrónica Exenta")
    FacturaCompraElectronica = (46, "Factura Compra Electrónica")
    GuiaDespachoElectronica = (52, "Guia Despacho Electrónica")
    NotaDebitoElectronica = (56, "Nota Debito Electrónica")
    NotaCreditoElectronica = (61, "Nota Credito Electrónica")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class DTEFacturasType(Enum):
    NotSet = (0, "No Asignado")
    FacturaElectronica = (33, "Factura Electrónica")
    FacturaElectronicaExcenta = (34, "Factura Electrónica Exenta")
    FacturaCompraElectronica = (46, "Factura Compra Electrónica")
    LiquidacionFacturaElectronica = (43, "Liquidación Factura Electrónica")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]

class TipoDocumentoLibro(Enum):
    NotSet = (0, "No se ha definido un valor aún.")
    FacturaManual = (30, "Factura manual")
    FacturaExentaManual = (32, "Factura exenta manual")
    FacturaElectronica = (33, "Factura electrónica")
    FacturaExentaElectronica = (34, "Factura exenta electrónica")
    BoletaVentasServicios = (36, "Boletas de ventas y servicios")
    BoletaExenta = (38, "Boleta no afecta o exenta")
    BoletaElectronica = (39, "Boletas electrónica")
    LiquidacionFacturaManual = (40, "Liquidación Factura Manual")
    BoletaExentaElectronica = (41, "Boletas no afectas o exentas electrónicas")
    LiquidacionFacturaElectronica = (43, "Liquidación factura electrónica")
    FacturaCompra = (45, "Factura de compra")
    FacturaCompraElectronica = (46, "Factura de compra electrónica")
    NotaDebito = (55, "Nota de débito manual")
    NotaDebitoElectronica = (56, "Nota de débito electrónica")
    NotaCredito = (60, "Nota de crédito manual")
    NotaCreditoElectronica = (61, "Nota de crédito electrónica")
    FacturaExportacion = (101, "Factura de exportación")
    FacturaVentaExentaAZonaFrancaPrimaria = (102, "Factura de venta exenta a zona franca primaria")
    Liquidacion = (103, "Liquidación")
    NotaDebitoExportacion = (104, "Nota de débito de exportación")
    BoletaLiquidacion = (105, "Boletas liquidación")
    NotaCreditoExportacion = (106, "Nota de crédito de exportación")
    SRF = (108, "SRF: Solicitud de registro de factura")
    FacturaTurista = (109, "Factura a turista")
    LiquidacionRecibidaPorMandante = (900, "DEPRECATED! Liquidación recibida por el mandante")
    FacturaVentaaEmpresasTerritorioPreferencial = (901, "Factura de ventas a empresas del territorio preferencial")
    ConocimientoEmbarque = (902, "Conocimiento de Embarque")
    DUS = (903, "Documento Único de Salida (DUS)")
    ZonaFranca_FacturaTraspaso = (904, "Factura de traspaso")
    FacturaReexpedicion = (905, "Factura de reexpedición")
    BoletaVentaModuloZonaFranca = (906, "Boletas de venta Modulos Zona Franca")
    FacturaVentaModuloZonaFranca = (907, "Facturas de venta Módulos Zona Franca")
    ZonaFranca_FacturaVentaModuloZF = (909, "Facturas venta módulo Zona franca")
    ZonaFranca_SolicitudTrasladoZF = (910, "Solicitud de traslado Zona Franca")
    DeclaracionIngresoZonaFrancaPrimaria = (911, "Declaración de ingreso a Zona Franca Primaria")
    DIN = (914, "Declaración de Ingreso")
    DeclaracionIngresoZonaFranca = (918, "DEPRECATED! Declaración de Ingreso de Zona Franca")
    ResumenVentasNacionalesPasajesSinFactura = (919, "Resumen Ventas de nacionales pasajes sin Factura")
    OtroRegistroAumentaDebito = (920, "Otros registros no documentados. Aumenta débito.")
    LiquidacionRecibidaMandatario = (921, "DEPRECATED! Liquidación recibida por mandatario")
    OtrosRegistrosDisminuyeDebito = (922, "Otros registros. Disminuye débito.")
    FacturaExportacionElectronica = (110, "Factura de Exportación Electrónica")
    NotaDebitoExportacionElectronica = (111, "Nota de Débito de Exportación Electrónica")
    NotaCreditoExportacionElectronica = (112, "Nota de Crédito de Exportación Electrónica")
    ResumenVentasInternacionalPasajesSinFactura = (924, "Resumen ventas de internacionales pasajes sin Factura")
    AjusteAumentoTipoCambio = (500, "Ajuste aumento Tipo de Cambio")
    AjusteDisminucionTipoCambio = (501, "Ajuste disminución Tipo de Cambio")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
