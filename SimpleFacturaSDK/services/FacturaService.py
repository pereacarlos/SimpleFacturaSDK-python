import os
import json
import logging
from typing import List
from SimpleFacturaSDK.Utilidades.Simplificar_error import simplificar_errores
from requests_toolbelt import MultipartEncoder
import requests
from SimpleFacturaSDK.models.GetFactura.Dte import Dte
from SimpleFacturaSDK.models.GetFactura.ReporteDTE import ReporteDTE
from SimpleFacturaSDK.models.ResponseDTE import Response
from SimpleFacturaSDK.enumeracion.TipoSobreEnvio import TipoSobreEnvio
from SimpleFacturaSDK.models.GetFactura.InvoiceData import InvoiceData
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales

class FacturacionService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url


    def obtener_pdf(self, solicitud):
        url = f"{self.base_url}/dte/pdf"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def obtener_timbre(self, solicitud):
        url = f"{self.base_url}/dte/timbre"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            #timbre_data = json.loads(response.content)
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def obtener_xml(self, solicitud):
        url = f"{self.base_url}/dte/xml"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )
    
    def obtener_dte(self, solicitud) -> Response[Dte]:
        url = f"{self.base_url}/documentIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[Dte].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def obtener_sobreXml(self, solicitud, sobre) -> bytes:
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
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=response.content)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def facturacion_individualV2_Dte(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def facturacion_individualV2_Boletas(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/invoiceV2/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text                
        if response.status_code == 200:
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )
    
    def facturacion_individualV2_Exportacion(self, solicitud, sucursal) -> Response[InvoiceData]:
        if not isinstance(sucursal, str):
            return Response(
                status=400,
                message="El parámetro 'sucursal' debe ser un string.",
                data=None
            )
        url = f"{self.base_url}/dte/exportacion/{sucursal}"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def facturacion_Masiva(self, credenciales: Credenciales, path_csv: str):
        url = f"{self.base_url}/massiveInvoice"
        if not os.path.isfile(path_csv):
            return Response(
                status=400,
                message="El archivo no existe.",
                data=None
            )
        solicitud_dict = serializar_solicitud_dict(credenciales)
        m = MultipartEncoder(
            fields={
                'data': json.dumps(solicitud_dict),
                'input': ('archivo.csv', open(path_csv, 'rb'), 'text/csv')
            }
        )
        headers = {
            'Content-Type': m.content_type
        }
        response = self.session.post(url, headers=headers, data=m)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            return Response(status=200, data=contenidoRespuesta)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def EmisionNC_ND_V2(self, solicitud, sucursal, motivo) -> Response[InvoiceData]:
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
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text        
        if response.status_code == 200:
            deserialized_response = Response[InvoiceData].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def listadoDteEmitidos(self, solicitud) -> Response[List[Dte]]:
        url = f"{self.base_url}/documentsIssued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[Dte]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def enviarCorreo(self, solicitud) -> bool:
        url = f"{self.base_url}/dte/enviar/mail"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[bool].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        return Response(
            status=response.status_code,
            message=simplificar_errores(contenidoRespuesta),
            data=None
        )

    def consolidadoVentas(self, solicitud) -> Response[List[ReporteDTE]]:
        url = f"{self.base_url}/dte/consolidated/issued"
        solicitud_dict = serializar_solicitud_dict(solicitud)
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[List[ReporteDTE]].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        else:
           return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )

    def ConciliarEmitidos(self, solicitud, mes, anio) -> Response[str]:
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
        response = self.session.post(url, json=solicitud_dict)
        contenidoRespuesta = response.text
        if response.status_code == 200:
            deserialized_response = Response[str].parse_raw(contenidoRespuesta)
            return Response(status=200, data=deserialized_response.data)
        else:
            return Response(
                status=response.status_code,
                message=simplificar_errores(contenidoRespuesta),
                data=None
            )
            