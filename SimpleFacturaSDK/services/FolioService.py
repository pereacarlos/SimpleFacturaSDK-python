from typing import List, Optional
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.Folios.FoliosAnulablesEnt import FoliosAnulablesEnt
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
from SimpleFacturaSDK.models.Folios.TimbrajeEnt import TimbrajeEnt, TimbrajeApiEnt
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

    def SolicitarFolios(self, solicitud) -> Optional[TimbrajeApiEnt]:
        url = f"{self.base_url}/folios/solicitar"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=TimbrajeApiEnt)
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")

    #Corregir
    def ConsultarFolios(self, solicitud) -> Optional[TimbrajeApiEnt]:
        url = f"{self.base_url}/folios/consultar"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            resultado = Response.from_dict(response_json, data_type=TimbrajeApiEnt)
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")