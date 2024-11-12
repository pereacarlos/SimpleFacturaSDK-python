from typing import List
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import ReceptorExternoEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ClientesService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def CrearClientes(self, solicitud) -> List[ReceptorExternoEnt]:
        url = f"{self.base_url}/addClients"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response.from_dict(response_json, data_type=ReceptorExternoEnt)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()

'''
    def ListarClientes(self, solicitud) -> ProductoExternoEnt:
        url = f"{self.base_url}/products"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        
        if response.status_code == 200:
            response_json = response.json()
            print("Respuesta completa:", response_json)
            deserialized_response = Response.from_dict(response_json, data_type=ProductoExternoEnt)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()'''