from typing import List, Optional
from models.Folios.FoliosAnulablesEnt import FoliosAnulablesEnt
from models.Folios.TimbrajeEnt import TimbrajeEnt, TimbrajeApiEnt
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
import requests
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp

class FolioService:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def ConsultaFoliosDisponibles(self, solicitud) -> int:
        url = f"{self.base_url}/folios/consultar/disponibles"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[int].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=deserialized_response.data)
                return Response(
                    status=response.status,
                    message=simplificar_errores(contenidoRespuesta),
                    data=None
                )
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
                data=None
            )

    async def SolicitarFolios(self, solicitudFolio) -> Optional[TimbrajeApiEnt]:
        url = f"{self.base_url}/folios/solicitar"
        solicitud_dict = serializar_solicitud_dict(solicitudFolio)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[TimbrajeApiEnt].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=deserialized_response.data)
                return Response(
                    status=response.status,
                    message=simplificar_errores(contenidoRespuesta),
                    data=None
                )
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
                data=None
            )

    async def ConsultarFolios(self, solicitud) -> Optional[Response[List[TimbrajeApiEnt]]]:
        url = f"{self.base_url}/folios/consultar"
        solicitud_dict = serializar_solicitud_dict(solicitud)       
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[TimbrajeApiEnt]].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=deserialized_response.data)
                return Response(
                    status=response.status,
                    message=simplificar_errores(contenidoRespuesta),
                    data=None
                )
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
                data=None
            )
    
    async def Folios_Sin_Uso(self, solicitud) -> Optional[Response[List[FoliosAnulablesEnt]]]:
        url = f"{self.base_url}/folios/consultar/sin-uso"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[FoliosAnulablesEnt]].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=deserialized_response.data)
                return Response(
                    status=response.status,
                    message=simplificar_errores(contenidoRespuesta),
                    data=None
                )
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
                data=None
            )

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()