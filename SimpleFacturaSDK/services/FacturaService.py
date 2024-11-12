import os
import json
from requests_toolbelt import MultipartEncoder
import requests
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.enumeracion.TipoSobreEnvio import TipoSobreEnvio
from SimpleFacturaSDK.models.GetFactura.InvoiceData import InvoiceData
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

class FacturacionService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url


    def obtener_pdf(self, solicitud):
        url = f"{self.base_url}/dte/pdf"
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def obtener_timbre(self, solicitud):
        url = f"{self.base_url}/dte/timbre"
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def obtener_xml(self, solicitud):
        url = f"{self.base_url}/dte/xml"
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def obtener_sobreXml(self, solicitud, sobre) -> bytes:
        if isinstance(sobre, int):
            try:
                sobre_enum = TipoSobreEnvio(sobre)
                sobre_value = sobre_enum.value
            except ValueError:
                allowed_values = [e.value for e in TipoSobreEnvio]
                raise ValueError(f"El valor numérico de 'sobre' debe ser uno de {allowed_values}, no '{sobre}'")
        else:
            raise ValueError("El parámetro 'sobre' debe ser un número entero.")

        url = f"{self.base_url}/dte/xml/sobre/{sobre_value}"
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text

        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def obtener_dte(self, solicitud) -> Dte:
        url = f"{self.base_url}/documentIssued"
        solicitud_dict =  solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=Dte)
             #print("Status:", resultado.status)
             #print("Message:", resultado.message)
             #print("DTE Data:", resultado.data) 
            return resultado.data
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")


    def facturacion_individualV2_Dte(self, solicitud, sucursal) -> InvoiceData:
        # Validar que la sucursal sea un string
        if not isinstance(sucursal, str):
            raise ValueError("El parámetro 'sucursal' debe ser un string.")
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    
    def facturacion_individualV2_Boletas(self, solicitud, sucursal) -> InvoiceData:
        # Validar que la sucursal sea un string
        if not isinstance(sucursal, str):
            raise ValueError("El parámetro 'sucursal' debe ser un string.")
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    
    def facturacion_individualV2_Exportacion(self, solicitud, sucursal) -> InvoiceData:
        # Validar que la sucursal sea un string
        if not isinstance(sucursal, str):
            raise ValueError("El parámetro 'sucursal' debe ser un string.")
        url = f"{self.base_url}/dte/exportacion/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()
   
    def facturacion_Masiva(self, credenciales: Credenciales, path_csv: str):
        url = f"{self.base_url}/massiveInvoice"
        if not os.path.isfile(path_csv):
            raise ValueError(f"El archivo '{path_csv}' no existe.")
        m = MultipartEncoder(
            fields={
                'data': json.dumps(credenciales.to_dict()),
                'input': ('archivo.csv', open(path_csv, 'rb'), 'text/csv')
            }
        )
        headers = {
            'Content-Type': m.content_type
        }
        response = self.session.post(url, headers=headers, data=m)
        contenido_respuesta = response.text
        print("Respuesta completa:", contenido_respuesta)

        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            raise Exception(f"Error en la petición: {contenido_respuesta}")
    
    def EmisionNC_ND_V2(self, solicitud, sucursal, motivo) -> InvoiceData:
        if not isinstance(sucursal, str):
            raise ValueError("El parámetro 'sucursal' debe ser un string.")

        if not isinstance(motivo, int):
            raise ValueError("El parámetro 'motivo' debe ser un número entero.")
        url = f"{self.base_url}/invoiceCreditDebitNotesV2/{sucursal}/{motivo}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)

        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()

    def listadoDteEmitidos(self, solicitud) -> Dte:
        url = f"{self.base_url}/documentsIssued"
        solicitud_dict = solicitud.to_dict()
        print("Solicitud:", solicitud_dict)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=Dte)
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")






