from enum import Enum

class TipoEnvio:
    class EnvioType(Enum):
        NotSet = 0
        EnvioDTE = 1
        EnvioBoleta = 2
        LVC = 3
        RVD = 4

    class ValidacionType(Enum):
        NotSet = 0
        DTE = 1
        EnvioDTE = 2
        EnvioBoleta = 3
        RVD = 4
        LibroGuias = 5
        LCV = 6