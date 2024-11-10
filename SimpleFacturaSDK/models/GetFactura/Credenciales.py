class Credenciales:
    def __init__(self, rut_emisor, nombre_sucursal=None, email_usuario=None, rut_contribuyente=None): 
        self.rut_emisor = rut_emisor
        self.nombre_sucursal = nombre_sucursal
        self.email_usuario = email_usuario
        self.rut_contribuyente = rut_contribuyente

    def to_dict(self):
        return {
            "RutEmisor": self.rut_emisor,
            "nombreSucursal": self.nombre_sucursal,
            "emailUsuario": self.email_usuario,
            "rutContribuyente": self.rut_contribuyente
        }
