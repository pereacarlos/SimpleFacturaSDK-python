from dataclasses import dataclass
from typing import Optional
from models.GetFactura.Dte import Dte

@dataclass
class ResponseDTE:
    status: int
    message: str
    data: Optional[Dte] = None
    errors: Optional[str] = None

    @classmethod
    def from_dict(cls, dict_data):
        data_field = dict_data.get('data')
        if data_field:
            data_field = Dte.from_dict(data_field)
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
            "data": self.data.to_dict() if self.data else None,
            "errors": self.errors
        }
