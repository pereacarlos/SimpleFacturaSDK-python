import json
from models.GetFactura.ResponseDTE import ResponseDTE
from requests import Response


class FacturacionService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def obtener_dte(self, solicitud) -> ResponseDTE:
        url = f"{self.base_url}/documentIssued"
        response = self.session.post(url, json=solicitud)
        contenidoRespuesta = response.text
        print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            response_json = response.json()
            resultado = ResponseDTE.from_dict(response_json)
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")


'''
    def obtener_pdf_dte(self, solicitud):
        url = "https://api.simplefactura.cl/dte/pdf"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")

    def obtener_timbre_dte(self, solicitud):
        url = "https://api.simplefactura.cl/dte/timbre"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
        

    def obtener_xml_dte(self, solicitud):
        url = "https://api.simplefactura.cl/dte/xml"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
        

    def obtener_dte(self, solicitud):
        url =  f"{self.base_url}/documentIssued"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
   
    def obtener_sobreXml(self, solicitud):
        url = "https://api.simplefactura.cl/dte/xml/sobre/0"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
    
    def facturacion_individualV2_Dte(self, solicitud):
        url = "https://api.simplefactura.cl/invoiceV2/Casa_Matriz"
        response = self.session.post(url, data=json.dumps(solicitud))
        
        if response.status_code == 200:
            return response.content
        else:
            error_message = response.json().get("errors", "Unknown error")
            raise Exception(f"Error en la petición: {error_message}")
        

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