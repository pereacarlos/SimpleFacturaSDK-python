import asyncio
from typing import List

from SimpleFacturaSDK.models.Payku.PaykuResponses import PaykuTransaccionResponse
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud_dict


class PaykuService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client

    async def transacciones(self, solicitud) -> Response[List[PaykuTransaccionResponse]]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/payku/transacciones"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[List[PaykuTransaccionResponse]].parse_raw(contenidoRespuesta)
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

    async def activar_desactivar(self, solicitud) -> Response[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/payku/activar-desactivar"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
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

    async def generar_url(self, solicitud) -> Response[str]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/payku/generar-url"
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

    async def reenviar_link_qr(self, solicitud) -> Response[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/payku/reenviar-link-Qr"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
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

    async def marcar_dte_pagado_o_pendiente(self, solicitud) -> Response[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/dte/marcar-pagado-pendiente"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
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

    async def close(self):
        if not self.session.closed:
            await self.session.close()

    def __del__(self):
        if hasattr(self, "session") and not self.session.closed:
            asyncio.run(self.close())
