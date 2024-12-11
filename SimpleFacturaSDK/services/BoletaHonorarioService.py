from typing import List, Optional
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.BHEEnt import BHEEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import requests
import aiohttp
import asyncio

class BoletaHonorarioService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client

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
        except Exception as error:
            return Response(
                status=500,
                message=error.__str__(),
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
        except Exception as error:
            return Response(
                status=500,
                message=error.__str__(),
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
        except Exception as error:
            return Response(
                status=500,
                message=error.__str__(),
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
        except Exception as error:
            return Response(
                status=500,
                message=error.__str__(),
                data=None
            )

    async def close(self):
        if not self.session.closed:
            await self.session.close()

    def __del__(self):
        if hasattr(self, 'session') and not self.session.closed:
            asyncio.run(self.close())