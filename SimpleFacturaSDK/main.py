from Base import APIClient 


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
    # Llamar al método para obtener el PDF
    pdf_bytes = client_api.Facturacion.obtener_pdf_dte(solicitud)
    ruta = "dte.pdf"  # Ruta donde se guardará el PDF
    with open(ruta, "wb") as f:
        f.write(pdf_bytes)
    print("El PDF se ha descargado correctamente.")
except Exception as ex:
    print(f"Error: {str(ex)}")
