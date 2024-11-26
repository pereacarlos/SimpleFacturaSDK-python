from typing import List
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest, ProductoExternoEnt
from SimpleFacturaSDK.models.Productos.ProductoEnt import ProductoEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp
import asyncio

class ProductoService:
    def __init__(self, base_url, headers, session=None):
        self.base_url = base_url
        self.headers = headers
        self.session = session or aiohttp.ClientSession(headers=headers)

    async def CrearProducto(self, solicitud) -> Response[List[ProductoEnt]]:
        url = f"{self.base_url}/addProducts"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[ProductoEnt]].parse_raw(contenidoRespuesta)
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

        
    async def listarProductos(self, solicitud) -> Response[List[ProductoExternoEnt]]:
        url = f"{self.base_url}/products"
        solicitud_dict = solicitud.to_dict()
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[ProductoExternoEnt]].parse_raw(contenidoRespuesta)
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