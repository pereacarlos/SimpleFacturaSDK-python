from typing import List, Optional
from SimpleFacturaSDK.models.ResponseDTE import Response
import requests
from SimpleFacturaSDK.models.SerializarJson import serializar_solicitud, serializar_solicitud_dict,dataclass_to_dict


class ConfiguracionService:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url