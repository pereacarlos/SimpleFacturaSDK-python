from enum import Enum
import json

class ListaProveedorEnum(Enum):
    ListaNegra = 1
    ListaBlanca = 2
    Desconocido = 3

    def descripcion(self):
        descripcion = {
            1: "Lista Negra",
            2: "Lista Blanca",
            3: "Desconocido"
        }

        return descripcion.get(self.value, "Proveedor no definido")
