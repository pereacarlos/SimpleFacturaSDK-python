from typing import List
from SimpleFacturaSDK.models.Folios import Foliorequest,FoliosAnulablesEnt,SolicitudFolios,TimbrajeEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class FolioService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def ConsultaFoliosDisponibles(self, solicitud) -> int:
        url = f"{self.base_url}/folios/consultar/disponibles"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[int].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()