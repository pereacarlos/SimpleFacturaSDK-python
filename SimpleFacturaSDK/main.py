
from SimpleFacturaSDK.Base import APIClient
import base64
import json
#from requests.auth import HTTPBasicAuth
#from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
#from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
#from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

#from SimpleFacturaSDK.models.GetFactura.Documento import Documento
from SimpleFacturaSDK.models.GetFactura.Exportaciones import Exportaciones
from SimpleFacturaSDK.models.GetFactura.OtraMoneda import OtraMoneda
from SimpleFacturaSDK.models.GetFactura.Extranjero import Extranjero
from SimpleFacturaSDK.models.GetFactura.Aduana import Aduana
from SimpleFacturaSDK.models.GetFactura.Transporte import Transporte
from SimpleFacturaSDK.models.GetFactura.Chofer import Chofer
from SimpleFacturaSDK.models.GetFactura.TipoBulto import TipoBulto
from SimpleFacturaSDK.enumeracion.CodigosAduana import Paises,Moneda, ModalidadVenta, ClausulaCompraVenta, ViasdeTransporte, Puertos, UnidadMedida, TipoBultoEnum
from SimpleFacturaSDK.models.GetFactura.Encabezado import Encabezado
from SimpleFacturaSDK.models.GetFactura.IdentificacionDTE import IdDoc
from SimpleFacturaSDK.models.GetFactura.Emisor import Emisor
from SimpleFacturaSDK.models.GetFactura.Receptor import Receptor
from SimpleFacturaSDK.models.GetFactura.Totales import Totales
from SimpleFacturaSDK.models.GetFactura.Detalle import Detalle
from SimpleFacturaSDK.models.GetFactura.CodigoItem import CdgItem
from SimpleFacturaSDK.enumeracion.TipoDTE import DTEType
from SimpleFacturaSDK.enumeracion.IndicadorServicio import IndicadorServicioEnum
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
from SimpleFacturaSDK.models.ResponseDTE import Response


username = "demo@chilesystems.com"
password = "Rv8Il4eV"
client_api = APIClient(username, password)
credenciales = Credenciales(
    rut_emisor="76269769-6",
    nombre_sucursal="Casa Matriz"
)

path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional.csv"

try:
    factura = client_api.Facturacion.facturacion_Masiva(credenciales, path_csv)
 
    print("\nDatos de la Respuesta:")
    print(f"Status: {factura.get('status')}")
    print(f"Message: {factura.get('message')}")
    print(f"Data: {factura.get('data')}")
except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
    print("Detalle del error:", http_err.response.text)
except Exception as err:
    print(f"Error: {err}")