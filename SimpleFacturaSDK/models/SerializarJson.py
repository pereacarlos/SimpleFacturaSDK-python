from typing import Type, TypeVar, Any, Optional
from SimpleFacturaSDK.models.GetFactura.RequestDTE import RequestDTE
from dataclasses import asdict,is_dataclass,fields
import json
from enum import Enum
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