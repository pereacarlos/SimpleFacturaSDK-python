from Base import APIClient 
import base64
import json


# Datos de autenticación
username = "demo@chilesystems.com"
password = "Rv8Il4eV"

# Crear instancia del cliente API
client_api = APIClient(username, password)

# Crear la solicitud
solicitud = {
    "Credenciales": {
        "RutEmisor": "76269769-6",
        "NombreSucursal": "Casa Matriz"
    },
    "DteReferenciadoExterno": {
        "Folio": 4117,
        "CodigoTipoDte": 33,
        "Ambiente": 0
    }
}


try:
    
    # Obtener DTE
    dte_bytes = client_api.Facturacion.obtener_dte(solicitud)
    ruta = "dte.json"  # Ruta donde se guardará el DTE
    with open(ruta, "wb") as f:
        f.write(dte_bytes)
    print("El DTE se ha descargado correctamente.")

    



except Exception as ex:
    print(f"Error: {str(ex)}")

