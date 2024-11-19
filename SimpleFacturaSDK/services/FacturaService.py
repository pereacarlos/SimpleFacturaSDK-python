
import os
import json
from typing import List
from Utilidades.Simplificar_error import simplificar_errores
from requests_toolbelt import MultipartEncoder
import aiofiles
import requests
from models.GetFactura.Dte import Dte
from models.GetFactura.ReporteDTE import ReporteDTE
from models.ResponseDTE import Response
from enumeracion.TipoSobreEnvio import TipoSobreEnvio
from models.GetFactura.InvoiceData import InvoiceData
from models.GetFactura.RequestDTE import RequestDTE
from models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from models.GetFactura.Credenciales import Credenciales
import httpx
import aiohttp
import traceback
from httpx import AsyncClient



class FacturacionService:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.session = httpx.AsyncClient(base_url=base_url, headers=headers)

    async def _post_and_response_facturacion(self, url: str, solicitud_dict: dict) -> Response[InvoiceData]:
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener Facturacion",
                data=None
            )

    async def obtener_pdf(self, solicitud):
        url = f"{self.base_url}/dte/pdf"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                return Response(status=200, data=response.content)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener PDF",
                data=None
            )
    async def obtener_timbre(self, solicitud):
        url = f"{self.base_url}/dte/timbre"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                return Response(status=200, data=response.content)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener timbre",
                data=None
            )
    async def obtener_xml(self, solicitud):
        url = f"{self.base_url}/dte/xml"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                return Response(status=200, data=response.content)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener XML",
                data=None
            )
    async def obtener_dte(self, solicitud) -> Response[Dte]:
        url = f"{self.base_url}/documentIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[Dte].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener XML",
                data=None
            )
        
    async def obtener_sobreXml(self, solicitud, sobre) -> bytes:
        if isinstance(sobre, int):
            try:
                sobre_enum = TipoSobreEnvio(sobre)
                sobre_value = sobre_enum.value
            except ValueError:
                allowed_values = [e.value for e in TipoSobreEnvio]
                return Response(
                    status=400,
                    message=f"El parámetro 'sobre' debe ser uno de los siguientes valores: {allowed_values}",
                    data=None
                )
        else:
            return Response(
                status=400,
                message="El parámetro 'sobre' debe ser un número entero.",
                data=None
            )
        url = f"{self.base_url}/dte/xml/sobre/{sobre_value}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                return Response(status=200, data=response.content)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener XML",
                data=None
            )
   
    async def facturacion_individualV2_Dte(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        return await self._post_and_response_facturacion(url, solicitud_dict)
        
    async def facturacion_individualV2_Boletas(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        return await self._post_and_response_facturacion(url, solicitud_dict)
    
    async def facturacion_individualV2_Exportacion(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/dte/exportacion/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        return await self._post_and_response_facturacion(url, solicitud_dict)

    async def facturacion_Masiva(self, credenciales: Credenciales, path_csv: str):
        url = f"{self.base_url}/massiveInvoice"
        if not os.path.isfile(path_csv):
            return Response(status=400, message="El archivo no existe.", data=None)

        solicitud_dict = serializar_solicitud_dict(credenciales)
        solicitud_json = json.dumps(solicitud_dict)

        try:
            async with aiohttp.ClientSession(headers=self.headers) as session:
                data = aiohttp.FormData()
                data.add_field('data', solicitud_json, content_type='application/json')

                with open(path_csv, 'rb') as f:
                    data.add_field('input', f, filename='archivo.csv', content_type='text/csv')

                    async with session.post(url, data=data) as response:
                        contenidoRespuesta = await response.text()

                        if response.status == 200:
                            print("Response Content:", contenidoRespuesta)
                            return Response(status=200, data=contenidoRespuesta)
                        else:
                            return Response(
                                status=response.status,
                                message=simplificar_errores(contenidoRespuesta),
                                data=None
                            )
        except Exception as e:
            print(f"An exception occurred: {e}")
            traceback.print_exc()
            return Response(
                status=500,
                message="Error al obtener Facturación",
                data=None
            )

    async def EmisionNC_ND_V2(self, solicitud, sucursal, motivo) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
           return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        if not isinstance(motivo, int):
            return Response(
                status=400,
                message="El parámetro 'motivo' debe ser un número entero.",
                data=None
            )
        url = f"{self.base_url}/invoiceCreditDebitNotesV2/{sucursal}/{motivo}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener Emision",
                data=None
            )

    async def listadoDteEmitidos(self, solicitud) -> Response[List[Dte]]:
        url = f"{self.base_url}/documentsIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[List[Dte]].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener Listado",
                data=None
            )

    
    async def enviarCorreo(self, solicitud) -> Response[bool]:
        url = f"{self.base_url}/dte/enviar/mail"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        print(solicitud_dict)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            print(response)
            contenidoRespuesta = response.text
            print(contenidoRespuesta)
            if response.status_code == 200:
                deserialized_response = Response[bool].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al enviar Correo",
                data=None
            )
        
    async def consolidadoVentas(self, solicitud) -> Response[List[ReporteDTE]]:
        url = f"{self.base_url}/dte/consolidated/issued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[List[ReporteDTE]].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener Consolidado",
                data=None
            )
    
    async def ConciliarEmitidos(self, solicitud, mes, anio):
        url = f"{self.base_url}/documentsIssued/consolidate/{mes}/{anio}"
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
        print(solicitud_dict)
        try:
            response = await self.session.post(url, json=solicitud_dict)
            print(response)
            contenidoRespuesta = response.text
            if response.status_code == 200:
                deserialized_response = Response[str].parse_raw(contenidoRespuesta)
                return Response(status=200, data=deserialized_response.data)
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
        except httpx.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return Response(
                status=500,
                message="Error al obtener Conciliar",
                data=None
            )
            
    async def close(self):
        await self.session.aclose()