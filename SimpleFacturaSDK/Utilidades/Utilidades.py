from enumeracion.TipoDTE import DTEType
from enumeracion.FormaPago import FormaPagoEnum
from dataclasses import dataclass, field, asdict
import base64

@dataclass
class Utilidades:

    def ObtenerNombreTipoDTE(tipoDTE: DTEType) -> str:
        tipo: str = "NOT SET"
        if tipoDTE == DTEType.FacturaCompraElectronica:
            tipo = "FACTURA DE COMPRA ELECTRONICA"
        elif tipoDTE == DTEType.FacturaElectronica:
            tipo = "FACTURA ELECTRONICA"
        elif tipoDTE == DTEType.FacturaElectronicaExenta:
            tipo = "FACTURA ELECTRONICA EXENTA"
        elif tipoDTE == DTEType.GuiaDespachoElectronica:
            tipo = "GUIA DESPACHO ELECTRONICA"
        elif tipoDTE == DTEType.NotaCreditoElectronica:
            tipo = "NOTA DE CREDITO ELECTRONICA"
        elif tipoDTE == DTEType.NotaDebitoElectronica:
            tipo = "NOTA DEBITO ELECTRONICA"
        elif tipoDTE == DTEType.BoletaElectronica:
            tipo = "BOLETA ELECTRONICA"
        elif tipoDTE == DTEType.BoletaElectronicaExenta:
            tipo = "BOLETA ELECTRONICA EXENTA"
        elif tipoDTE == DTEType.LiquidacionFacturaElectronica:
            tipo = "LIQUIDACION FACTURA ELECTRONICA"
        elif tipoDTE == DTEType.FacturaExportacionElectronica:
            tipo = "FACTURA DE EXPORTACION ELECTRONICA"
        elif tipoDTE == DTEType.NotaCreditoExportacionElectronica:
            tipo = "NOTA DE CREDITO DE EXPORTACION ELECTRONICA"
        elif tipoDTE == DTEType.NotaDebitoExportacionElectronica:
            tipo = "NOTA DE DEBITO DE EXPORTACION ELECTRONICA"
        return tipo

    def ObtenerNombreTipoDTE(tipoDTE: DTEType) -> str:
        tipo: str = "NOT SET"
        if tipoDTE == DTEType.FacturaCompraElectronica:
            tipo = "FACTURA DE COMPRA ELECTRÓNICA"
        elif tipoDTE == DTEType.FacturaElectronica:
            tipo = "FACTURA ELECTRÓNICA"
        elif tipoDTE == DTEType.FacturaElectronicaExenta:
            tipo = "FACTURA ELECTRÓNICA EXENTA"
        elif tipoDTE == DTEType.GuiaDespachoElectronica:
            tipo = "GUIA DESPACHO ELECTRÓNICA"
        elif tipoDTE == DTEType.NotaCreditoElectronica:
            tipo = "NOTA DE CRÉDITO ELECTRÓNICA"
        elif tipoDTE == DTEType.NotaDebitoElectronica:
            tipo = "NOTA DÉBITO ELECTRÓNICA"
        elif tipoDTE == DTEType.BoletaElectronica:
            tipo = "BOLETA ELECTRÓNICA"
        elif tipoDTE == DTEType.BoletaElectronicaExenta:
            tipo = "BOLETA ELECTRÓNICA EXENTA"
        elif tipoDTE == DTEType.FacturaExportacionElectronica:
            tipo = "FACTURA DE EXPORTACIÓN"
        elif tipoDTE == DTEType.NotaDebitoExportacionElectronica:
            tipo = "NOTA DÉBITO DE EXPORTACIÓN"
        elif tipoDTE == DTEType.NotaCreditoExportacionElectronica:
            tipo = "NOTA CRÉDITO DE EXPORTACIÓN"
        elif tipoDTE == DTEType.NotSet:
            tipo = "DOCUMENTO DE PROVEEDORES"
        elif tipoDTE == DTEType.LiquidacionFacturaElectronica:
            tipo = "LIQUIDACIÓN DE ELECTRONICA"
        return tipo

   