from typing import  Optional
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.models.EmisorApiEnt import EmisorAapiEnt
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
import aiohttp
import asyncio
import os
import json

class ConfiguracionService:
    def __init__(self, base_url, headers, session, client):
        self.base_url = base_url
        self.headers = headers
        self.session = session
        self.client = client


    async def datos_empresa(self, solicitud) -> Optional[EmisorAapiEnt]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/datosEmpresa"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            async with self.session.post(url, json=solicitud_dict) as response:
                contenidoRespuesta = await response.text()
                if response.status == 200:
                    deserialized_response = Response[EmisorAapiEnt].parse_raw(contenidoRespuesta)
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
    
    async def subir_Certificado_Digital(self, credenciales: Credenciales, certificado: str) -> Optional[bool]:
        await self.client.ensure_token_valid()
        url = f"{self.base_url}/certificado/subir"
        if not os.path.isfile(certificado):
            return Response(status=400, message="El archivo no existe.", data=False)

        solicitud_dict = serializar_solicitud_dict(credenciales)
        solicitud_json = json.dumps(solicitud_dict)

        try:
            data = aiohttp.FormData()
            data.add_field('certificadoData', solicitud_json, content_type='application/json')

            with open(certificado, 'rb') as f:
                data.add_field('certificado', f, filename='certificado.pfx', content_type='application/x-pkcs12')

                async with self.session.post(url, data=data) as response:
                    contenidoRespuesta = await response.text()

                    if response.status == 200:
                        return Response(status=200, data=True, message="Certificado digital cargado exitosamente. La validación de vigencia y operatividad se realizará automáticamente por el sistema")
                    else:
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
        if hasattr(self, 'session') and not self.session.closed:
            asyncio.run(self.close())