from enum import Enum


class PlanUsuarioEnum(Enum):
    Independiente = 100
    Pyme = 200
    Avanzado = 300
    Premium = 400

    def descripcion(self):
        descripcion = {
            100: "Independiente",
            200: "Pyme",
            300: "Avanzado",
            400: "Premium",
        }
        return descripcion.get(self.value, "Plan no definido")
