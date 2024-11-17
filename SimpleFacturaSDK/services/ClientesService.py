from typing import List, Optional
from models.Clientes.NuevoReceptorExternoRequest import ReceptorExternoEnt
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
import requests
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ClientesService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def CrearClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/addClients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def ListarClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/clients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )