from typing import List, Optional
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.EmisorApiEnt import EmisorAapiEnt
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ConfiguracionService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url


    def datos_empresa(self, solicitud) -> Optional[EmisorAapiEnt]:
        url = f"{self.base_url}/datosEmpresa"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[EmisorAapiEnt].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")
            response.raise_for_status()