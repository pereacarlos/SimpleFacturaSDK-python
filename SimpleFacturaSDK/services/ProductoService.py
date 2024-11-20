from typing import List
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest, ProductoExternoEnt
from models.Productos.ProductoEnt import ProductoEnt
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp

class ProductoService:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = aiohttp.ClientSession(headers=self.headers)

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
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
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
        except aiohttp.ClientError as err:
            return Response(
                status=500,
                message=f"Error en la conexión: {err}",
                data=None
            )

    async def close(self):
        await self.session.close()