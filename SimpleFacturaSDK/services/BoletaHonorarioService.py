from typing import List, Optional
from models.BoletaHonorarios.BHERequest import BHERequest
from models.BoletaHonorarios.BHEEnt import BHEEnt
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
import requests
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class BoletaHonorarioService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def ObtenerPdf(self, solicitud) -> Response[bytes]:
        url = f"{self.base_url}/bhe/pdfIssuied"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict) 
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def ListadoBHEEmitidos(self, solicitud) -> Optional[list[BHEEnt]]:
        url = f"{self.base_url}/bhesIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[List[BHEEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def ObtenerPdfBoletaRecibida(self, solicitud) -> bytes:
        url = f"{self.base_url}/bhe/pdfReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict) 
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def ListadoBHERecibido(self, solicitud) -> Optional[list[BHEEnt]]:
        url = f"{self.base_url}/bhesReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[List[BHEEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )