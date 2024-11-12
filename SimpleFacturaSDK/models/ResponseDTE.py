from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    status: int
    message: str
    data: T
    errors: Optional[Any] = None

    @classmethod
    def from_dict(cls, data: dict, data_type: T) -> "Response":
        data = data.copy()
        data["data"] = data_type.from_dict(data["data"])
        return cls(**data)

