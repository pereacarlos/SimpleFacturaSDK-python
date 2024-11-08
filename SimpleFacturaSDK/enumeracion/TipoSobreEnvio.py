from enum import Enum

class TipoSobreEnvio(Enum):
    AlSII = (0, "Al SII")
    AlReceptor = (1, "Al Receptor")

    def __new__(cls, value, description):
        obj = object.__new__(cls)
        obj._value_ = value  # Asignamos el valor interno del Enum
        obj.description = description  # Asignamos la descripción
        return obj
