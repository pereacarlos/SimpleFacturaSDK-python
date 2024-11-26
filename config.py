import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("SF_BASE_URL", "https://api.simplefactura.cl")