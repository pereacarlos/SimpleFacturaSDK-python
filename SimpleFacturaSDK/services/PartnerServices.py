import asyncio
import json
import os
import mimetypes

from typing import List

import aiohttp

from SimpleFacturaSDK.models.ActividadesEconomicaApiEnt import ActividadesEconomicaEnt
from SimpleFacturaSDK.models.Partner.PartnerDteResumenRequest import PartnerDteResumenResponse
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud_dict

class PartnerService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client

    async def enrolamiento_empresa(self, solicitud) -> Response[str]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/partners/enrolamiento-empresa"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[str].parse_raw(contenidoRespuesta)
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
        
    async def obtener_actividades_economicas(self) -> Response[List[ActividadesEconomicaEnt]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/actividades-economicas"
        try:
            async with self.session.get(url) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[ActividadesEconomicaEnt]].parse_raw(contenidoRespuesta)
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
        
    async def upload_logo(self, credenciales, path_logo: str) -> Response[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/upload-logo"

        if not os.path.isfile(path_logo):
            return Response(status=400, message="El archivo no existe.", data=False)

        credenciales_dict = serializar_solicitud_dict(credenciales)
        credenciales_json = json.dumps(credenciales_dict, ensure_ascii=False)
        content_type, _ = mimetypes.guess_type(path_logo)
        if not content_type:
            content_type = "application/octet-stream"

        try:
            data = aiohttp.FormData()
            data.add_field("CredencialesJson", credenciales_json, content_type="application/json")

            with open(path_logo, "rb") as f:
                data.add_field(
                    "Logo",
                    f,
                    filename=os.path.basename(path_logo),
                    content_type=content_type,
                )

                async with self.session.post(url, data=data) as response:
                    contenidoRespuesta = await response.text()
                    if response.status == 200:
                        deserialized_response = Response[bool].parse_raw(contenidoRespuesta)
                        return Response(
                            status=200,
                            data=deserialized_response.data,
                            message=deserialized_response.message
                        )
                    return Response(
                        status=response.status,
                        message=simplificar_errores(contenidoRespuesta),
                        data=False
                    )
        except Exception as error:
            return Response(
                status=500,
                message=error.__str__(),
                data=False
            )
        
    async def obtener_resumen_dtes(self, solicitud) -> Response[PartnerDteResumenResponse]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/partners/dtes/resumen"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[PartnerDteResumenResponse].parse_raw(contenidoRespuesta)
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
        if hasattr(self, "session") and not self.session.closed:
            asyncio.run(self.close())
