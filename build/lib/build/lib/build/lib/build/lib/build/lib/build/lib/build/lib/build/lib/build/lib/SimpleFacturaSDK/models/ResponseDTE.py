from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class Response(BaseModel, Generic[T]):
    status: int
    message: Optional[str] = None 
    data: Optional[T] = None
    errors: Optional[Any] = None

    def success(cls, data: T) -> "Response[T]":
      
        return cls(status=200, data=data, message="Success", errors=None)

    @classmethod
    def error(cls, status_code: int, message: str, errors: Optional[Any] = None) -> "Response[T]":
       
        return cls(status=status_code, data=None, message=message, errors=errors)
