from typing import List, Optional
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import ReceptorExternoEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ClientesService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def CrearClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/addClients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()

    def ListarClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/clients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()