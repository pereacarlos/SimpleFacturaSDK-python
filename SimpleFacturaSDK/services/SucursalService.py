
from typing import List,Optional
from SimpleFacturaSDK.models.Sucursal import Sucursal
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

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
            return resultado
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()