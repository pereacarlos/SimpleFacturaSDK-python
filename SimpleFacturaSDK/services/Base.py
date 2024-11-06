import requests
import base64
import json

BASE_URL = "https://api.simplefactura.cl"

class APIClient:
    def __init__(self, username, password):
        self.base_url = BASE_URL
        self.session = requests.Session()
        
        # Manually set Authorization header with base64 encoding
        auth_token = f"{username}:{password}".encode("ascii")
        base64_auth_token = base64.b64encode(auth_token).decode("ascii")
        self.session.headers.update({
            'Authorization': f'Basic {base64_auth_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def obtener_pdf_dte(self, solicitud):
        url = f"{self.base_url}/dte/pdf"
        response = self.session.post(url, data=json.dumps(solicitud))
        print("Status Code:", response.status_code)  # Debugging line
        print("Response Text:", response.text)       # Debugging line
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Error en la petición: {response.text}")
