# auth_utils.py
import aiohttp
from datetime import datetime, timezone

async def obtener_y_configurar_token(client):
    token, expires_at = await obtener_token_jwt(client)
    client.token = token
    client.expires_at = expires_at
    client.headers['Authorization'] = f'Bearer {token}'

async def obtener_token_jwt(client):
    async with aiohttp.ClientSession() as session:
        url = f"{client.base_url}/token"
        payload = {
            "email": client.username,
            "password": client.password
        }

        async with session.post(url, json=payload) as response:
            data = await response.json()
            print("Respuesta completa:", data)  # Para depuración
            if response.status == 200:
                token = data.get("accessToken")
                if not token:
                    raise ValueError("No se recibió 'accessToken' en la respuesta del servidor.")
                
                expires_at_str = data.get("expiresAt")
                if not expires_at_str:
                    raise ValueError("No se recibió 'expiresAt' en la respuesta del servidor.")
                
                expires_at = datetime.fromisoformat(expires_at_str.replace("Z", "+00:00"))
                return token, expires_at
            else:
                text = await response.text()
                raise ValueError(f"No se pudo obtener el token. Status: {response.status}, Respuesta: {text}")

async def ensure_token_valid(client):
    if token_ha_expirado(client):
        await obtener_y_configurar_token(client)
        # Actualizar la sesión con el nuevo token
        await client.session.close()
        client.session = aiohttp.ClientSession(headers=client.headers)
        # Actualizar instancias de servicios con la nueva sesión
        for service_name, service_class in client.services:
            service_instance = getattr(client, service_name, None)
            if service_instance:
                service_instance.session = client.session
                service_instance.headers = client.headers

def token_ha_expirado(client):
    if client.expires_at is None:
        return True
    ahora = datetime.now(timezone.utc)
    return ahora >= client.expires_at
