from Base import APIClient
import base64
import json
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from models.GetFactura.SolicitudPdfDte import SolicitudPdfDte

def main():
    # Datos de autenticación
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"

    # Crear instancia del cliente API
    client_api = APIClient(username, password)

    solicitud = SolicitudPdfDte(
        credenciales=Credenciales(
            rut_emisor="76269769-6"
        ),
        dte_referenciado_externo=DteReferenciadoExterno(
            folio=12553,
            codigo_tipo_dte=39,
            ambiente=0
        )
    )
    try: 
        solicitud_dict = solicitud.to_dict() 
        # Obtener DTE
        dte_bytes = client_api.Facturacion.obtener_dte(solicitud_dict)
        ruta = "dte.json"
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(dte_bytes, f, default=lambda o: o.__dict__, ensure_ascii=False)
        
        print("El DTE se ha descargado correctamente.")
    except Exception as ex:
        print(f"Error: {str(ex)}")

if __name__ == "__main__":
    main()


