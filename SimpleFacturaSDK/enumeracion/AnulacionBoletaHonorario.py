from enum import Enum


class AnulacionBoletaHonorario(Enum):
    NotSet = 0
    ServicioNoPagado = 1
    ServicioNoEfectuado = 2
    ErrorDigitacion = 3

    def descripcion(self):
        descripcion = {
            0: "Sin Asignar",
            1: "No se efectuo el pago de los servicios por parte del receptor",
            2: "No se efectuo la prestacion de servicios",
            3: "Error en la digitacion",
        }
        return descripcion.get(self.value, "Motivo de anulacion no definido")
