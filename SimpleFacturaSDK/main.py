from services.Base import APIClient  # Assuming APIClient class is in Base.py
from models.GetPdf.SolicitudPdfDte import SolicitudPdfDte
import json

# Datos de autenticación
username = "demo@chilesystems.com"
password = "Rv8Il4eV"

# Crear instancia del cliente API
client_api = APIClient(username, password)

# Crear la solicitud con el campo 'Credenciales'
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
    pdf_bytes = client_api.obtener_pdf_dte(solicitud)
    ruta = "dte.pdf"  # Ruta donde se guardará el PDF
    with open(ruta, "wb") as f:
        f.write(pdf_bytes)
    print("El PDF se ha descargado correctamente.")
except Exception as ex:
    print(f"Error: {str(ex)}")
