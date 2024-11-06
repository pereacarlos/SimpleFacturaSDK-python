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
        "Documento": {
            "Encabezado": {
                "IdDoc": {
                    "TipoDTE": 33,
                    "FchEmis": "2024-09-05",
                    "FmaPago": 1,
                    "FchVenc": "2024-09-05"
                },
                "Emisor": {
                    "RUTEmisor": "76269769-6",
                    "RznSoc": "SERVICIOS INFORMATICOS CHILESYSTEMS EIRL",
                    "GiroEmis": "Desarrollo de software",
                    "Telefono": [
                        "912345678"
                    ],
                    "CorreoEmisor": "mvega@chilesystems.com",
                    "Acteco": [
                        620200
                    ],
                    "DirOrigen": "Calle 7 numero 3",
                    "CmnaOrigen": "Santiago",
                    "CiudadOrigen": "Santiago"
                },
                "Receptor": {
                    "RUTRecep": "17096073-4",
                    "RznSocRecep": "Hotel Iquique",
                    "GiroRecep": "test",
                    "CorreoRecep": "mvega@chilesystems.com",
                    "DirRecep": "calle 12",
                    "CmnaRecep": "Paine",
                    "CiudadRecep": "Santiago"
                },
                "Totales": {
                    "MntNeto": "832",
                    "TasaIVA": "19",
                    "IVA": "158",
                    "MntTotal": "990"
                }
            },
            "Detalle": [
                {
                    "NroLinDet": "1",
                    "NmbItem": "Alfajor",
                    "CdgItem": [
                        {
                            "TpoCodigo": "ALFA",
                            "VlrCodigo": "123"
                        }
                    ],
                    "QtyItem": "1",
                    "UnmdItem": "un",
                    "PrcItem": "831.932773",
                    "MontoItem": "832"
                }
            ]
        },
        "Observaciones": "NOTA AL PIE DE PAGINA",
        "TipoPago": "30 dias"
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
        print("Respuesta completa:", timbre_data)
        
            # Obtener XML
    xml_bytes = client_api.Facturacion.obtener_xml_dte(solicitud)
    ruta = "dte.xml"  # Ruta donde se guardará el XML
    with open(ruta, "wb") as f:
        f.write(xml_bytes)
    print("El XML se ha descargado correctamente.")

        # Obtener DTE
    dte_bytes = client_api.Facturacion.obtener_dte(solicitud)
    ruta = "dte.json"  # Ruta donde se guardará el DTE
    with open(ruta, "wb") as f:
        f.write(dte_bytes)
    print("El DTE se ha descargado correctamente.")

        # Obtener sobre XML
    sobre_xml_bytes = client_api.Facturacion.obtener_sobreXml(solicitud)
    ruta = "sobre.xml"  # Ruta donde se guardará el sobre XML
    with open(ruta, "wb") as f:
        f.write(sobre_xml_bytes)
    print("El sobre XML se ha descargado correctamente.")
        
        '''
    
    # Facturación individual
    response = client_api.Facturacion.facturacion_individualV2_Dte(solicitud)
    ruta = "factura.json"  # Ruta donde se guardará la factura
    with open(ruta, "wb") as f:
        f.write(response)
    print("La factura se ha descargado correctamente.")

    
    
    
    



except Exception as ex:
    print(f"Error: {str(ex)}")

