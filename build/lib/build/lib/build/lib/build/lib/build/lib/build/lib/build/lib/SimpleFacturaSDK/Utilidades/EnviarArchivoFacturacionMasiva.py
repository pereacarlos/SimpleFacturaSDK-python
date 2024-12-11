import aiohttp

async def enviar_archivo_con_datos(url: str, headers: dict, solicitud_json: str, path_csv: str):
    async with aiohttp.ClientSession(headers=headers) as session:
        data = aiohttp.FormData()
        data.add_field('data', solicitud_json, content_type='application/json')

        with open(path_csv, 'rb') as archivo:
            data.add_field('input', archivo, filename='archivo.csv', content_type='text/csv')

        async with session.post(url, data=data) as response:
            contenido_respuesta = await response.text()
            return response.status, contenido_respuesta
