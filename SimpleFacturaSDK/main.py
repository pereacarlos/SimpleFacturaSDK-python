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
    "Exportaciones": {
        "Encabezado": {
            "IdDoc": {
                "TipoDTE": 110,
                "FchEmis": "2023-10-17",
                "FmaPago": 1,
                "FchVenc": "2023-10-17"
            },
            "Emisor": {
                "RUTEmisor": "76269769-6",
                "RznSoc": "Chilesystems",
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
                "RUTRecep": "55555555-5",
                "RznSocRecep": "CLIENTE INTERNACIONAL EXP IMP",
                "Extranjero": {
                    "NumId": "331-555555",
                    "Nacionalidad": 331
                },
                "GiroRecep": "Giro de Cliente",
                "CorreoRecep": "amamani@chilesystems.com",
                "DirRecep": "Dirección de Cliente",
                "CmnaRecep": "Comuna de Cliente",
                "CiudadRecep": "Ciudad de Cliente"
            },
            "Transporte": {
                "Aduana": {
                    "CodModVenta": 1,
                    "CodClauVenta": 5,
                    "TotClauVenta": "1984.65",
                    "CodViaTransp": 4,
                    "CodPtoEmbarque": 901,
                    "CodPtoDesemb": 262,
                    "Tara": "1",
                    "CodUnidMedTara": 10,
                    "PesoBruto": "10.65",
                    "CodUnidPesoBruto": 6,
                    "PesoNeto": "9.56",
                    "CodUnidPesoNeto": 6,
                    "TotBultos": "30",
                    "TipoBultos": [
                        {
                            "CodTpoBultos": 75,
                            "CantBultos": "30",
                            "IdContainer": "1-2",
                            "Sello": "1-3",
                            "EmisorSello": "CONTENEDOR"
                        }
                    ],
                    "MntFlete": "965.1",
                    "MntSeguro": "10.25",
                    "CodPaisRecep": 224,
                    "CodPaisDestin": 224
                }
            },
            "Totales": {
                "TpoMoneda": 13,
                "MntExe": "1000",
                "MntTotal": "1000"
            },
            "OtraMoneda": {
                "TpoMoneda": 200,
                "TpoCambio": "800.36",
                "MntExeOtrMnda": "45454.36",
                "MntTotOtrMnda": "45454.36"
            }
        },
        "Detalle": [
            {
                "NroLinDet": "1",
                "CdgItem": [
                    {
                        "TpoCodigo": "INT1",
                        "VlrCodigo": "39"
                    }
                ],
                "IndExe": 1,
                "NmbItem": "CHATARRA DE ALUMINIO",
                "DscItem": "OPCIONAL",
                "QtyItem": "1",
                "UnmdItem": "U",
                "PrcItem": "1000",
                "MontoItem": "1000"
            }
        ]
    },
    "Observaciones": "NOTA AL PIE DE PAGINA"
};


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

      
    # Facturación individual
    response = client_api.Facturacion.facturacion_individualV2_Dte(solicitud)
    ruta = "factura.json"  # Ruta donde se guardará la factura
    with open(ruta, "wb") as f:
        f.write(response)
    print("La factura se ha descargado correctamente.")

    # Facturación individual boletas
    response = client_api.Facturacion.facturacion_individualV2_Boletas(solicitud)
    ruta = "boleta.json"  # Ruta donde se guardará la factura
    with open(ruta, "wb") as f:
        f.write(response)
    print("La factura se ha descargado correctamente.")
        
        '''
    
  



except Exception as ex:
    print(f"Error: {str(ex)}")

