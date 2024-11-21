from typing import List, Optional
from models.BoletaHonorarios.BHERequest import BHERequest
from models.BoletaHonorarios.BHEEnt import BHEEnt
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
import requests
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp

class BoletaHonorarioService:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def ObtenerPdf(self, solicitud) -> Response[bytes]:
        url = f"{self.base_url}/bhe/pdfIssuied"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.read()
                if response.status == 200:
                    return Response(status=200, data=contenidoRespuesta)
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

    async def ListadoBHEEmitidos(self, solicitud) -> Optional[list[BHEEnt]]:
        url = f"{self.base_url}/bhesIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[BHEEnt]].parse_raw(contenidoRespuesta)
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

    async def ObtenerPdfBoletaRecibida(self, solicitud) -> bytes:
        url = f"{self.base_url}/bhe/pdfReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.read()
                if response.status == 200:
                    return Response(status=200, data=contenidoRespuesta)
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

    async def ListadoBHERecibido(self, solicitud) -> Optional[list[BHEEnt]]:
        url = f"{self.base_url}/bhesReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[BHEEnt]].parse_raw(contenidoRespuesta)
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
        if not self.session.closed:
            await self.session.close()