import json

class FacturacionService:
    def __init__(self, session):
        self.session = session

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
        url = "https://api.simplefactura.cl/documentIssued"
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
