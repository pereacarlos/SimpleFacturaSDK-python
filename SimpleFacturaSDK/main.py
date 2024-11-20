import asyncio
from ClientSimpleFactura import ClientSimpleFactura
from models.GetFactura.Credenciales import Credenciales
async def main():
    username = "demo@chilesystems.com"
    password = "Rv8Il4eV"
    client_api = ClientSimpleFactura(username, password)
    credenciales = Credenciales(
        rut_emisor="76269769-6",
        nombre_sucursal="Casa Matriz"
    )
    path_csv = r"C:\Users\perea\Downloads\ejemplo_carga_masiva_nacional.csv"
    try:
        factura = await client_api.Facturacion.facturacion_Masiva(credenciales, path_csv)
        print("\nDatos de la Respuesta:")
        print(factura.data)
        print("Status Code:", factura.status)
        print("Message:", factura.message)
    except Exception as err:
        print(f"Error: {err}")
    finally:
        await client_api.Facturacion.close()
if __name__ == "__main__":
    asyncio.run(main())
