from enumeracion.TipoDTE import DTEType
from enumeracion.FormaPago import FormaPagoEnum
from dataclasses import dataclass, field, asdict
import base64
import xml.etree.ElementTree as ET
from xml.dom import minidom
from cryptography.hazmat.primitives.serialization import pkcs12
from OpenSSL import crypto
import platform
import subprocess

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

    def ObtenerNombreFormaPago(FormaPago: FormaPagoEnum) -> str:
        tipo: str = ""
        if FormaPago == FormaPagoEnum.NotSet:
            tipo = "No Aplica"
        elif FormaPago == FormaPagoEnum.Contado:
            tipo = "Contado"
        elif FormaPago == FormaPagoEnum.Credito:
            tipo = "Crédito"
        elif FormaPago == FormaPagoEnum.SinCosto:
            tipo = "Sin Costo"
        return tipo


    def crear_certificado_desde_bytearray(bytes_certificado, password):
        # Crear un objeto certificado X509 a partir de bytes y contraseña (compatible con multiplataforma)
        try:
            certificado = crypto.load_pkcs12(bytes_certificado, password.encode())
            return certificado
        except Exception as e:
            print(f"Error al cargar el certificado: {e}")
            return None

    def crear_xml_documento_desde_bytearray(bytes_xml):
        # Crear un documento XML a partir de bytes
        documento = minidom.parseString(bytes_xml)
        return documento

    def obtener_certificados_maquinas():
        # Obtener nombres de certificados del almacén de certificados de la máquina local
        certificados = []
        sistema = platform.system()
        if sistema == "Windows":
            # Windows: usa win32com para acceder a los certificados
            try:
                from win32com.client import Dispatch
                store = Dispatch("CAPICOM.Store")
                store.Open(2, "LocalMachine", 2)
                for cert in store.Certificates:
                    certificados.append(cert.FriendlyName)
                store.Close()
            except Exception as e:
                print(f"Error al acceder a los certificados en Windows: {e}")
        elif sistema == "Linux" or sistema == "Darwin":  # Darwin es macOS
            # Linux y MacOS: usar comandos de sistema para listar certificados
            try:
                result = subprocess.run(['ls', '/etc/ssl/certs'], capture_output=True, text=True)
                certificados = result.stdout.splitlines()
            except Exception as e:
                print(f"Error al acceder a los certificados en {sistema}: {e}")
        return certificados

    def obtener_certificados_usuario():
        # Obtener nombres de certificados del almacén de certificados del usuario actual
        certificados = []
        sistema = platform.system()
        if sistema == "Windows":
            try:
                from win32com.client import Dispatch
                store = Dispatch("CAPICOM.Store")
                store.Open(2, "CurrentUser", 2)
                for cert in store.Certificates:
                    certificados.append(cert.FriendlyName)
                store.Close()
            except Exception as e:
                print(f"Error al acceder a los certificados de usuario en Windows: {e}")
        elif sistema == "Linux" or sistema == "Darwin":  # Darwin es macOS
            try:
                # Intentar acceder a certificados de usuario en Linux/Mac
                result = subprocess.run(['ls', '/etc/ssl/certs'], capture_output=True, text=True)
                certificados = result.stdout.splitlines()
            except Exception as e:
                print(f"Error al acceder a los certificados de usuario en {sistema}: {e}")
        return certificados

    def convert_encode(text):
        # Escapar caracteres especiales en texto
        return ET.Element('root', {'text': text}).attrib['text']

    def encode_to_iso88591(text):
        # Convertir texto a ISO-8859-1 con entidades XML
        iso_encoded = text.encode("ISO-8859-1", errors="xmlcharrefreplace").decode("ISO-8859-1")
        result = iso_encoded.replace('"', "&quot;")\
                            .replace('&', "&amp;")\
                            .replace("'", "&apos;")\
                            .replace('<', "&lt;")\
                            .replace('>', "&gt;")
        return result

    
        