from typing import List, Optional
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ProveedorService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def listarDteRecibidos(self, solicitud) -> Response[Optional[List[Dte]]]:
        url = f"{self.base_url}/documentsReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[Dte]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def obtenerXml(self, solicitud) -> Response[bytes]:
        url = f"{self.base_url}/documentReceived/xml"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud.to_dict())
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def obtener_pdf(self, solicitud):
        url = f"{self.base_url}/documentReceived/getPdf"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()

    def ConciliarRecibidos(self, solicitud, mes, anio) -> str:
        url = f"{self.base_url}/documentsReceived/consolidate/{mes}/{anio}"
        # deben de ser tipo número
        if not isinstance(mes, int):
            raise ValueError("El parámetro 'mes' debe ser un número entero.")
        if not isinstance(anio, int):
            raise ValueError("El parámetro 'anio' debe ser un número entero.")
        
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialize_response = Response[str].parse_raw(contenidoRespuesta)
            return deserialize_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()