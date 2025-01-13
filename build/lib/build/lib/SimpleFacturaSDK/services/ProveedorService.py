from typing import List, Optional
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.TrazasEnt import TrazasEnt
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
import aiohttp
import asyncio

class ProveedorService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client

    #Revisar
    async def Aceptar_RechazarDTE(self, solicitud) -> Response[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/acknowledgmentReceipt"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        print(solicitud_dict)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    return Response(status=200, data=True)
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

    async def listarDteRecibidos(self, solicitud) -> Response[Optional[List[Dte]]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/documentsReceived"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[Dte]].parse_raw(contenidoRespuesta)
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

    async def obtenerXml(self, solicitud) -> Response[bytes]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/documentReceived/xml"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    return Response(status=200, data=await response.read())
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
    
    async def obtener_pdf(self, solicitud) -> Response[bytes]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/documentReceived/getPdf"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.read()
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

    async def ConciliarRecibidos(self, solicitud, mes, anio) -> str:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/documentsReceived/consolidate/{mes}/{anio}"
        if not isinstance(mes, int):
            return Response(
                status=400,
                message="El parámetro 'mes' debe ser un número entero.",
                data=None
            )
        if not isinstance(anio, int):
            return Response(
                status=400,
                message="El parámetro 'anio' debe ser un número entero.",
                data=None
            )
        
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialize_response = Response[str].parse_raw(contenidoRespuesta)
                    return Response(status=200, data=deserialize_response.data)
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


    async def obtener_TrazasRecibidas(self, solicitud)-> Response[List[TrazasEnt]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/dte/trazasReceived"
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


    async def close(self):
        if not self.session.closed:
            await self.session.close()

    def __del__(self):
        if hasattr(self, 'session') and not self.session.closed:
            asyncio.run(self.close())
