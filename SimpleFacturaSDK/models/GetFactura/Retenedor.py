from dataclasses import dataclass

@dataclass
class Retenedor:
    """
    Clase que representa el retenedor del documento.
    """

    IndAgente: str = ''
    """Indicador agente retenedor."""

    MntBaseFaena: int = 0
    """Monto base faenamiento."""

    MntMargComer: int = 0
    """Márgenes de comercialización."""

    PrcConsFinal: int = 0
    """Precio unitario neto consumidor final."""

    def __init__(self):
        self.IndAgente = ''
        self.MntBaseFaena = 0
        self.MntMargComer = 0
        self.PrcConsFinal = 0