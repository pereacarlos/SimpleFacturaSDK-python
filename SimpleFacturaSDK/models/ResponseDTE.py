from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None
    errors: Optional[Any] = None

    @classmethod
    def from_dict(cls, dict_data, data_type: Optional[type] = None):
        data_field = dict_data.get('data')
        if data_field and data_type:
            data_field = data_type.from_dict(data_field)
        return cls(
            status=dict_data.get('status'),
            message=dict_data.get('message'),
            data=data_field,
            errors=dict_data.get('errors')
        )

 