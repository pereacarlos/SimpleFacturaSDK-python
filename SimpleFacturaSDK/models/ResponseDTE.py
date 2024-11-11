from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    status: int
    message: str
    data: T
    errors: Optional[Any] = None

