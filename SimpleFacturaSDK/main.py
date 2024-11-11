from dataclasses import asdict,is_dataclass,fields
import json
from SimpleFacturaSDK.models.GetFactura import RequestDTE, Documento,Encabezado,IdentificacionDTE,Emisor,Receptor,Totales,Detalle,CdgItem
from enumerados.DTEType import DTEType
import requests
from requests.auth import HTTPBasicAuth
from enum import Enum
from typing import Any
from typing import Type, TypeVar, Any, Optional
from Response import ResponseModel,InvoiceDataModel
T = TypeVar('T')

def dataclass_to_dict(obj: Any) -> Any:
    if is_dataclass(obj):
        result = {}
        for field in obj.__dataclass_fields__:
            value = getattr(obj, field)
            if value is not None:  # Omitir campos con valor None
                converted_value = dataclass_to_dict(value)
                # Solo agregar al resultado si no es None
                if converted_value is not None:
                    result[field] = converted_value
        return result
    elif isinstance(obj, Enum):
        return obj.value  # Cambia a obj.description() si prefieres la descripción
    elif isinstance(obj, list):
        return [dataclass_to_dict(item) for item in obj if item is not None]
    else:
        return obj
def serializar_solicitud(solicitud: RequestDTE) -> str:
    solicitud_dict = dataclass_to_dict(solicitud)
    solicitud_json = json.dumps(solicitud_dict, ensure_ascii=False, indent=4)
    return solicitud_json

def serializar_solicitud_dict(solicitud: RequestDTE) -> dict:
    return dataclass_to_dict(solicitud)
# Creación directa del objeto RequestDTE con objetos anidados

solicitud = RequestDTE(
    Documento=Documento(
        Encabezado=Encabezado(
            IdDoc=IdDoc(
                TipoDTE=DTEType.FacturaElectronica,
                FchEmis="2024-09-05",
                FmaPago=1,
                FchVenc="2024-09-05"
            ),
            Emisor=Emisor(
                RUTEmisor="76269769-6",
                RznSoc="SERVICIOS INFORMATICOS CHILESYSTEMS EIRL",
                GiroEmis="Desarrollo de software",
                Telefono=["912345678"],
                CorreoEmisor="mvega@chilesystems.com",
                Acteco=[620200],
                DirOrigen="Calle 7 numero 3",
                CmnaOrigen="Santiago",
                CiudadOrigen="Santiago"
            ),
            Receptor=Receptor(
                RUTRecep="17096073-4",
                RznSocRecep="Hotel Iquique",
                GiroRecep="test",
                CorreoRecep="mvega@chilesystems.com",
                DirRecep="calle 12",
                CmnaRecep="Paine",
                CiudadRecep="Santiago"
            ),
            Totales=Totales(
                MntNeto="832",
                TasaIVA="19",
                IVA="158",
                MntTotal="990"
            )
        ),
        Detalle=[
            Detalle(
                NroLinDet="1",
                NmbItem="Alfajor",
                CdgItem=[
                    CdgItem(
                        TpoCodigo="ALFA",
                        VlrCodigo="123"
                    )
                ],
                QtyItem="1",
                UnmdItem="un",
                PrcItem="831.932773",
                MontoItem="832"
            )
        ]
    ),
    Observaciones="NOTA AL PIE DE PAGINA",
    TipoPago="30 dias"
)
solicitud_diccionario = serializar_solicitud_dict(solicitud)
print(solicitud_diccionario) #solicitud en json
url = "https://api.simplefactura.cl/invoiceV2/Casa_Matriz"
headers = {
    "Content-Type": "application/json",
}
try:
    response = requests.post(
        url,
        json=solicitud_diccionario,  # Usamos json para que requests serialice automáticamente
        headers=headers,
        auth=HTTPBasicAuth('demo@chilesystems.com', 'Rv8Il4eV')  # Si utilizas autenticación básica
    )

    response.raise_for_status()  # Lanza una excepción para códigos de estado 4xx/5xx
    #print("Solicitud enviada exitosamente.")
    #print("Respuesta del servidor:", response.json())
    #response_content = response.text
    #response_dict = json.loads(response_content)    # Convertir la respuesta a dict
    # Deserializar a Response<InvoiceData>
    #deserialized_response = from_dict(Response[InvoiceData], response_dict)
    print("Solicitud enviada exitosamente.")
    response_content = response.text
    print("Respuesta JSON:")
    print(response_content)

    # Deserializar la respuesta usando Pydantic
    deserialized_response = ResponseModel[InvoiceDataModel].parse_raw(response_content)

    print("\nDatos de la Respuesta:")
    print(f"Status: {deserialized_response.status}")
    print(f"Message: {deserialized_response.message}")
    print(f"TipoDTE: {deserialized_response.data.tipoDTE}")
    print(f"RUT Emisor: {deserialized_response.data.rutEmisor}")
    print(f"RUT Receptor: {deserialized_response.data.rutReceptor}")
    print(f"Folio: {deserialized_response.data.folio}")
    print(f"Fecha Emision: {deserialized_response.data.fechaEmision}")
    print(f"Total: {deserialized_response.data.total}")
    print(deserialized_response.data)


except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print("Detalle del error:", response.text)
except Exception as err:
    print(f"An error occurred: {err}")
