from typing import List, Optional
from SimpleFacturaSDK.models.Clientes.NuevoReceptorExternoRequest import ReceptorExternoEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
import requests
import asyncio
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp

class ClientesService:
    def __init__(self, base_url, headers, session=None):
        self.base_url = base_url
        self.headers = headers
        self.session = session or aiohttp.ClientSession(headers=headers)

    async def CrearClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/addClients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
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

    async def ListarClientes(self, solicitud) -> Optional[List[ReceptorExternoEnt]]:
        url = f"{self.base_url}/clients"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[ReceptorExternoEnt]].parse_raw(contenidoRespuesta)
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