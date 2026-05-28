# SimpleFacturaSDK

SDK oficial en Python para integrar tus sistemas con SimpleFactura (ChileSystems): facturación, clientes, productos, proveedores, folios, boletas de honorarios, cesión, partner y Payku.

## Características

- Cliente asincrónico basado en `aiohttp`.
- Servicios separados por dominio (`Facturacion`, `Productos`, `Clientes`, etc.).
- Modelos tipados para requests/responses.
- Manejo de autenticación y renovación de token.

## Requisitos

- Python `>=3.6`
- `pip`

## Instalación

Desde PyPI:

```bash
pip install SimpleFacturaSDK
```

Para desarrollo local:

```bash
git clone https://github.com/pereacarlos/SimpleFacturaSDK-python.git
cd SimpleFacturaSDK-python
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz de tu proyecto:

```env
SF_USERNAME=tu_usuario
SF_PASSWORD=tu_contraseña
SF_BASE_URL=https://api.simplefactura.cl
```

Opcional: archivo `config.py` (si quieres forzar URL base por código):

```python
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("SF_BASE_URL", "https://api.simplefactura.cl")
```

## Uso rápido

```python
import asyncio
import os
from dotenv import load_dotenv
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura

load_dotenv()

username = os.getenv("SF_USERNAME")
password = os.getenv("SF_PASSWORD")

async def main():
    async with ClientSimpleFactura(username, password) as client:
        # Servicios disponibles
        facturacion = client.Facturacion
        productos = client.Productos
        proveedores = client.Proveedores
        clientes = client.Clientes
        sucursales = client.Sucursales
        folios = client.Folios
        configuracion = client.ConfiguracionService
        bhe = client.BoletaHonorarioService
        usuarios = client.Usuarios
        cesion = client.CesionService
        partner = client.PartnerService
        payku = client.PaykuService

        print("Cliente inicializado correctamente")

if __name__ == "__main__":
    asyncio.run(main())
```

## Ejemplo: obtener PDF de DTE

```python
import asyncio
from SimpleFacturaSDK.client_simple_factura import ClientSimpleFactura
from SimpleFacturaSDK.models.GetFactura.Credenciales import Credenciales
from SimpleFacturaSDK.models.GetFactura.DteReferenciadoExterno import DteReferenciadoExterno
from SimpleFacturaSDK.models.GetFactura.SolicitudPdfDte import SolicitudPdfDte


async def main():
    async with ClientSimpleFactura("usuario", "password") as client:
        solicitud = SolicitudPdfDte(
            credenciales=Credenciales(
                rut_emisor="76269769-6",
                nombre_sucursal="Casa Matriz",
            ),
            dte_referenciado_externo=DteReferenciadoExterno(
                folio=4117,
                codigoTipoDte=33,
                ambiente=0,
            ),
        )

        resp = await client.Facturacion.obtener_pdf(solicitud)
        if resp.status == 200:
            with open("factura.pdf", "wb") as f:
                f.write(resp.data)
            print("PDF guardado")
        else:
            print(f"Error {resp.status}: {resp.message}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Ejecutar tests

```bash
python -m unittest discover -s SimpleFacturaSDK/tests -p "test_*.py" -v
```

## Cobertura

Si ejecutas tests con cobertura y aparece:

```text
ModuleNotFoundError: No module named 'coverage'
```

instala la dependencia en el mismo intérprete que usa VS Code:

```bash
python -m pip install coverage
```

Luego puedes correr, por ejemplo:

```bash
python -m coverage run -m unittest discover -s SimpleFacturaSDK/tests -p "test_*.py"
python -m coverage report -m
```

## Problemas comunes

- `Credenciales incorrectas`: revisa `SF_USERNAME` y `SF_PASSWORD`.
- `SF_BASE_URL` no definida: asegúrate de tener `.env` o `config.py` correctamente configurado.
- VS Code usa otro Python: selecciona el intérprete correcto en `Python: Select Interpreter`.

## Documentación oficial

- Sitio SimpleFactura: [https://www.simplefactura.cl/](https://www.simplefactura.cl/)
- Documentación API (Postman): [https://documentacion.simplefactura.cl/](https://documentacion.simplefactura.cl/)
