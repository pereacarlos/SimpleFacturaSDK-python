import requests
from typing import List,Optional
from models.Sucursal import Sucursal
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from models.GetFactura.Credenciales import Credenciales
import aiohttp
import asyncio
class SucursalService:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = aiohttp.ClientSession(headers=self.headers)

    async def ListarSucursales(self, solicitud) -> Optional[List[Sucursal]]:
        url = f"{self.base_url}/branchOffices"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    resultado = Response[List[Sucursal]].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=resultado.data)
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

    def __del__(self):
        if not self.session.closed:
            asyncio.create_task(self.close())

    
