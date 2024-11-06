class Credenciales:
    def __init__(self, rut_emisor, nombre_sucursal):
        self.rut_emisor = rut_emisor
        self.nombre_sucursal = nombre_sucursal

    def to_dict(self):
        return {
            "rutEmisor": self.rut_emisor,
            "nombreSucursal": self.nombre_sucursal
        }
