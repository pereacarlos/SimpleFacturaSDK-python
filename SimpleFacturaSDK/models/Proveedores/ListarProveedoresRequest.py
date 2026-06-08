from dataclasses import dataclass


@dataclass
class ListarProveedoresRequest:
    RutEmisor: str

    def to_dict(self):
        return {
            "RutEmisor": self.RutEmisor,
        }
