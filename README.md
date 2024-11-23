# SDK SimpleFactura

El SDK SimpleFactura es una solución en Python diseñada para facilitar la integración con los servicios de SimpleFactura, parte de ChileSystems. Este SDK provee un conjunto de clases y métodos que permiten realizar operaciones como facturación, gestión de productos, proveedores, clientes, sucursales, folios, Datos de empresa y boletas de honorarios.

---

## Características principales

- **Simplifica** la interacción con los servicios de SimpleFactura.
- Proporciona interfaces específicas para operaciones como:
  - **Facturación**: Generación y gestión de documentos tributarios electrónicos.
  - **Gestión** de productos, proveedores y clientes.
  - **Gestión de folios**.
  - **Emisión de boletas de honorarios**.
- Compatible con **Python 3.6 y superior**.

---

## Requisitos

### Dependencias

Las dependencias necesarias para utilizar este SDK son:

- `requests`
- `aiohttp`
- `requests-toolbelt`
- `pydantic`
- `httpx`
- `pytest`
- `requests-mock`
- `python-dotenv`
- `pytest-asyncio`

### Plataforma

El SDK es compatible con **Python 3.6** y versiones superiores.

---

## Instalación

Puedes instalar el SDK y sus dependencias utilizando **pip**:
```bash
pip install SimpleFacturaSDK-python
```

Si necesitas instalar las dependencias manualmente:
    
```bash
pip install requests requests-toolbelt pydantic aiohttp pytest requests-mock python-dotenv pytest-asyncio httpx aiofiles

```

Opcional(Clonar el repositorio e instalar dependencias desde requirements.txt)
```bash
git clone https://github.com/pereacarlos/SimpleFacturaSDK-python.git
cd SimpleFacturaSDK-python
pip install -r requirements.txt

```
Cómo empezar
Para utilizar el SDK, simplemente inicializa la clase ClientSimpleFactura proporcionando tu nombre de usuario y contraseña:
```bash
from ClientSimpleFactura import ClientSimpleFactura
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")

def main():
    client_api = ClientSimpleFactura(username, password)
    
    # Ejemplo: Uso de los servicios
    facturacionService = client_api.Facturacion
    productoService = client_api.Productos
    proveedorService = client_api.Proveedores
    clientesService = client_api.Clientes
    sucursalService = client_api.Sucursales
    folioService = client_api.Folios
    configuracionService = client_api.ConfiguracionService
    boletaHonorarioService = client_api.BoletaHonorarioService

if __name__ == "__main__":
    main()

```

Ejemplo de uso: Obtener PDF de una factura
El siguiente ejemplo muestra cómo obtener el PDF de una factura utilizando el SDK:
```bash

import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.GetFactura.Credenciales import Credenciales
from models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from models.GetFactura.SolicitudPdfDte import SolicitudPdfDte
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")

async def main():
    client_api = ClientSimpleFactura(username, password)
    
    solicitud = SolicitudPdfDte(
        credenciales=Credenciales(
            rut_emisor="tu_rut_emisor",
            nombre_sucursal="tu_sucursal"
        ),
        dte_referenciado_externo=DteReferenciadoExterno(
            folio=4117,
            codigoTipoDte=33,
            ambiente=0
        )
    )
    
    try:
        pdf_response = await client_api.Facturacion.obtener_pdf(solicitud)
        if pdf_response.status == 200:
            with open("factura.pdf", "wb") as file:
                file.write(pdf_response.data)
            print("PDF guardado exitosamente")
        else:
            print(f"Error: {pdf_response.message}")
    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Facturacion.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Documentación
La documentación relevante para usar este SDK es:

- Documentación general:
  [Sitio Simple Factura](https://www.simplefactura.cl/).
- Documentacion de APIs [Postman](https://documentacion.simplefactura.cl/).
