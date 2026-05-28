from typing import List
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
import asyncio
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.TrazasEnt import TrazasEnt

class CesionService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client

    async def ceder_Factura(self, solicitud) -> Response[str]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/cederFactura"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    return Response(status=200, data=contenidoRespuesta)
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
        
    async def obtener_TrazasCesionEmitida(self, solicitud) -> Response[List[TrazasEnt]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/cessions/trazasIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[TrazasEnt]].parse_raw(contenidoRespuesta)
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

    async def listado_CesionesEmitidas(self, solicitud) -> Response[List[object]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/cessions/Issued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[object]].parse_raw(contenidoRespuesta)
                    return Response(
                        status=200,
                        data=deserialized_response.data,
                        message=deserialized_response.message
                    )
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
