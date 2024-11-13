from typing import List
from SimpleFacturaSDK.models.Productos.NuevoProductoExternoRequest import NuevoProductoExternoRequest, ProductoExternoEnt
from SimpleFacturaSDK.models.Productos.DatoExternoRequest import DatoExternoRequest
from SimpleFacturaSDK.models.Productos.ProductoEnt import ProductoEnt
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ProductoService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def CrearProducto(self, solicitud) -> ProductoEnt:
        url = f"{self.base_url}/addProducts"
        solicitud_dict = solicitud.to_dict()
        print("Solicitud dict:", solicitud_dict)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response.from_dict(response_json, data_type=ProductoEnt)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()  # La

    def listarProductos(self, solicitud) -> ProductoExternoEnt:
        url = f"{self.base_url}/products"
        solicitud_dict = solicitud.to_dict()
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        
        if response.status_code == 200:
            response_json = response.json()
            print("Respuesta completa:", response_json)
            deserialized_response = Response.from_dict(response_json, data_type=ProductoExternoEnt)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()