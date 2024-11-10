import json
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.enumeracion.TipoSobreEnvio import TipoSobreEnvio
from SimpleFacturaSDK.models.GetFactura.InvoiceData import InvoiceData
from SimpleFacturaSDK.enumeracion.CodigosAduana import CustomJSONEncoder
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE

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
        response = self.session.post(url, json=solicitud)
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
        
        solicitud_json = json.dumps(solicitud, cls=CustomJSONEncoder)
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        response = self.session.post(url, json=json.loads(solicitud_json))
        
        contenidoRespuesta = response.text
        print(f"Respuesta completa: {solicitud_json}")
        ruta = "jsonsolicitud.json"
        with open(ruta, "w") as archivo:
            archivo.write(solicitud_json)
            
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=InvoiceData)
            return resultado.data
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
    










'''

    def facturacion_individualV2_Dte(self, solicitud):
        url = "https://api.simplefactura.cl/invoiceV2/Casa_Matriz"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
    
    def facturacion_individualV2_Boletas(self, solicitud):
        url = "https://api.simplefactura.cl/invoiceV2/Casa_Matriz"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
    
    def facturacion_individualV2_Exportacion(self, solicitud):
        url = f"{self.base_url}/invoiceV2/Casa_Matriz"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
'''