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
    '''Obtener PDF y timbre

    pdf_bytes = client_api.Facturacion.obtener_pdf_dte(solicitud)
    ruta = "dte.pdf"  # Ruta donde se guardará el PDF
    with open(ruta, "wb") as f:
        f.write(pdf_bytes)
    print("El PDF se ha descargado correctamente.")

    timbre_response = client_api.Facturacion.obtener_timbre_dte(solicitud)
    
    timbre_data = json.loads(timbre_response)
    
    if 'data' in timbre_data:
        timbre_base64 = timbre_data['data']

        timbre_bytes = base64.b64decode(timbre_base64)
        
        # Save as PNG
        with open("timbre.png", "wb") as file:
            file.write(timbre_bytes)
        
        print("Timbre obtenido correctamente y guardado como timbre.png")
    else:
        print("Error: No se encontró la clave 'data' en la respuesta.")
        print("Respuesta completa:", timbre_data)'''

except Exception as ex:
    print(f"Error: {str(ex)}")

