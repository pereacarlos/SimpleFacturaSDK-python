# SimpleFacturaSDK/models/GetPdf/RespuestaPdfDte.py

class RespuestaPdfDte:
    def __init__(self, pdf_base64):
        self._pdf_base64 = pdf_base64

    @property
    def pdf_base64(self):

        return self._pdf_base64

    @pdf_base64.setter
    def pdf_base64(self, value):
        self._pdf_base64 = value

    def to_dict(self):

        return {
            "pdf_base64": self._pdf_base64
        }

    def save_to_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(self._pdf_base64)
