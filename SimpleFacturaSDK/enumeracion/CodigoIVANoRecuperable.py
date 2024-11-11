from enum import Enum
import json

class CodigoIVANoRecuperableEnum(Enum):
    NotSet = 0
    ComprasDestinadasAGenerarOperacioneExentas = 1
    FacturasRegistradasFueraPlazo = 2
    GastosRechazados = 3
    EntregaGratuita = 4
    Otros = 9

    def descripcion(self):
        description = {
            0: "",
            1: "Compras destinadas a generar operaciones no gravadas o exentas",
            2: "Facturas registradas fuera de plazo",
            3: "Gastos rechazados",
            4: "Entrega gratuita",
            9: "Otros"
        }

        return description.get(self.value, "")