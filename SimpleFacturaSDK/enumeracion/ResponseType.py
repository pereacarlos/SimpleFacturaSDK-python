from enum import Enum

class ResponseType(Enum):
    Accepted = 3
    AcceptedWithQualms = 4
    Rejected = 5

    def description(self):
        descriptions = {
            3: "Aceptado",
            4: "Aceptado con reparos",
            5: "Rechazado"
        }
        return descriptions.get(self.value, "")