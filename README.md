SDK SimpleFactura
El SDK SimpleFactura es una solución en Python diseñada para facilitar la integración con los servicios de SimpleFactura, parte de ChileSystems. Este SDK provee un conjunto de clases y métodos que permiten realizar operaciones como facturación, gestión de productos, proveedores, clientes, sucursales, folios, configuración y boletas de honorarios.

Características principales
Simplifica la interacción con los servicios de SimpleFactura.
Proporciona interfaces específicas para operaciones como:
Facturación: Generación y gestión de documentos tributarios electrónicos.
Gestión de productos, proveedores y clientes.
Gestión de folios.
Emisión de boletas de honorarios.
Compatible con Python 3.6 y superior.
Requisitos
Dependencias
Las dependencias necesarias para utilizar este SDK son:

cryptography
pyOpenSSL
requests-toolbelt
pydantic
aiohttp
httpx
pytest
requests-mock
python-dotenv
pytest-asyncio
Plataforma
El SDK es compatible con Python 3.6 y versiones superiores.

Instalación
Puedes instalar el SDK y sus dependencias utilizando pip:

bash
Copiar código
pip install simplefactura-sdk
Si necesitas instalar las dependencias manualmente:

bash
Copiar código
pip install cryptography pyOpenSSL requests-toolbelt pydantic aiohttp httpx pytest requests-mock python-dotenv pytest-asyncio
Cómo empezar
Para utilizar el SDK, inicializa la clase SimpleFacturaClient proporcionando tu nombre de usuario y contraseña:

python
Copiar código
from simplefactura_sdk import SimpleFacturaClient

def main():
    simplefactura_client = SimpleFacturaClient("usuario", "contraseña")
    # Ejemplo: Uso de los servicios
    facturacion_service = simplefactura_client.facturacion
    productos_service = simplefactura_client.productos
    proveedores_service = simplefactura_client.proveedores
    clientes_service = simplefactura_client.clientes
    sucursal_service = simplefactura_client.sucursal
    folio_service = simplefactura_client.folio
    configuracion_service = simplefactura_client.configuracion
    boleta_honorarios_service = simplefactura_client.boletas_honorarios

if __name__ == "__main__":
    main()
Documentación
La documentación relevante para usar este SDK es:

Documentación general: Sitio SimpleFactura
Documentación de APIs: Postman Collection
