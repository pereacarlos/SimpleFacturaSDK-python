from typing import List
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ProveedorService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def listarDteRecibidos(self, solicitud) -> Dte:
        url = f"{self.base_url}/documentsReceived"
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


    def obtenerXml(self, solicitud) -> Response[bytes]:
        url = f"{self.base_url}/documentReceived/xml"
        solicitud_dict = solicitud.to_dict()
        print("Solicitud:", solicitud_dict)
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def obtener_pdf(self, solicitud):
        url = f"{self.base_url}/documentReceived/getPdf"
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    def ConciliarRecibidos(self, solicitud, mes, anio) -> str:
        url = f"{self.base_url}/documentsReceived/consolidate/{mes}/{anio}"
        # deben de ser tipo número
        if not isinstance(mes, int):
            raise ValueError("El parámetro 'mes' debe ser un número entero.")
        if not isinstance(anio, int):
            raise ValueError("El parámetro 'anio' debe ser un número entero.")
        
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=str)
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")