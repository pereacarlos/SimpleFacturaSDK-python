import requests
from typing import List,Optional
from models.Sucursal import Sucursal
from models.ResponseDTE import Response
from Utilidades.Simplificar_error import simplificar_errores
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from models.GetFactura.Credenciales import Credenciales

class SucursalService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def ListarSucursales(self, solicitud) -> Optional[List[Sucursal]]:
        url = f"{self.base_url}/branchOffices"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text                
        if response.status_code == 200:
            resultado = Response[List[Sucursal]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=resultado.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )
