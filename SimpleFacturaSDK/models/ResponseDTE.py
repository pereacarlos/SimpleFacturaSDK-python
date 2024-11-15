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
    
    @classmethod
    def from_dict(cls, d: dict, data_type: Any) -> "Response":
        data = d["data"]
        
        if isinstance(data, list):
            if hasattr(data_type, 'from_dict'):
                data = [data_type.from_dict(item) for item in data]
            else:
                data = [data_type(item) for item in data]
        elif isinstance(data, dict):
            if hasattr(data_type, 'from_dict'):
                data = data_type.from_dict(data)
            else:
                data = data_type(**data)
        else:
            data = data_type(data)
        
        return cls(
            status=d["status"],
            message=d["message"],
            data=data,
            errors=d.get("errors")
        )