from typing import List
from models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest, ProductoExternoEnt
from models.Productos.DatoExternoRequest import DatoExternoRequest
from models.Productos.ProductoEnt import ProductoEnt
from models.ResponseDTE import Response
import requests
from Utilidades.Simplificar_error import simplificar_errores
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ProductoService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def CrearProducto(self, solicitud) -> Response[List[ProductoEnt]]:
        url = f"{self.base_url}/addProducts"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[ProductoEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def listarProductos(self, solicitud) -> Response[List[ProductoExternoEnt]]:
        url = f"{self.base_url}/products"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[ProductoExternoEnt]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )