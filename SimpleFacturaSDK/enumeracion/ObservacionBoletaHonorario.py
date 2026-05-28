from enum import Enum


class ObservacionBoletaHonorario(Enum):
    NotSet = 0
    NoReconoceRelacion = 1
    NoReconoceEmisor = 2

    def descripcion(self):
        descripcion = {
            0: "Sin Asignar",
            1: "No se reconoce la relacion contractual o comercial con el emisor.",
            2: "No se reconoce al emisor de la BHE.",
        }
        return descripcion.get(self.value, "Observacion no definida")
