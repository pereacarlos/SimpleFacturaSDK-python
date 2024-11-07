from dataclasses import dataclass, asdict
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")

@dataclass
class Response(Generic[T]):
    status: int
    message: str
    data: Optional[T] = None
    errors: Optional[object] = None

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

    def to_dict(self):
        return {
            "status": self.status,
            "message": self.message,
            "data": self.data.to_dict() if hasattr(self.data, 'to_dict') else self.data,
            "errors": self.errors
        }
