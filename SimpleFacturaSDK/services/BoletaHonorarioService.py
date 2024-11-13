from typing import List, Optional
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.models.BoletaHonorarios.BHEEnt import BHEEnt
from SimpleFacturaSDK.models.BoletaHonorarios.ListaBHERequest import ListaBHERequest
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class BoletaHonorarioService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def ObtenerPdf(self, solicitud) -> bytes:
        url = f"{self.base_url}/bhe/pdfIssuied"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict) 
        contenidoRespuesta = response.text
        #print("Respuesta completa:", contenidoRespuesta)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")


    def ListadoBHEEmitidos(self, solicitud) -> Optional[list[BHEEnt]]:
        url = f"{self.base_url}/bhesIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        
        contenidoRespuesta = response.text        
        print("Respuesta completa:", contenidoRespuesta)
        
        if response.status_code == 200:
            response_json = response.json()
            deserialized_response = Response[List[BHEEnt]].parse_raw(contenidoRespuesta)
            return deserialized_response
        else:
            raise Exception(f"Error en la petición: {contenidoRespuesta}")