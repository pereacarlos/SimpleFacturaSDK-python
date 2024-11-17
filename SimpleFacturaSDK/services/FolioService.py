from typing import List, Optional
from SimpleFacturaSDK.models.Folios.Foliorequest import FolioRequest
from SimpleFacturaSDK.models.Folios.FoliosAnulablesEnt import FoliosAnulablesEnt
from SimpleFacturaSDK.models.Folios.SolicitudFolios import SolicitudFolios
from SimpleFacturaSDK.models.Folios.TimbrajeEnt import TimbrajeEnt, TimbrajeApiEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
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
        if response.status_code == 200:
            deserialized_response = Response[int].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def SolicitarFolios(self, solicitudFolio) -> Optional[TimbrajeApiEnt]:
        url = f"{self.base_url}/folios/solicitar"
        solicitud_dict = serializar_solicitud_dict(solicitudFolio)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[TimbrajeApiEnt].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def ConsultarFolios(self, solicitud) -> Optional[Response[List[TimbrajeApiEnt]]]:
        url = f"{self.base_url}/folios/consultar"
        solicitud_dict = serializar_solicitud_dict(solicitud)       
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[TimbrajeApiEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def Folios_Sin_Uso(self, solicitud) -> Optional[Response[List[FoliosAnulablesEnt]]]:
        url = f"{self.base_url}/folios/consultar/sin-uso"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[FoliosAnulablesEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )