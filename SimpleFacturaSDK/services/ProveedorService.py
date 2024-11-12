from typing import List
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
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