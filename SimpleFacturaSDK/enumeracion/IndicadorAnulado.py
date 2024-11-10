from enum import Enum
import json
class IndicadorAnuladoEnum(Enum):
    NotSet = (0, "")
    Anulado = (1, "El estado del documento es ANULADO")
    AnuladoPrevio = (1, "Anulado Previo a su Envio al SII. Sólo para Guias de Despacho Electrónicas")
    AnuladoPosterior = (2, "Anulado Posterior a su Envio al SII. Sólo para Guias de Despacho Electrónicas")
    RecibidoParcialmente = (3, "Productos recibidos parcialmente. Sólo para Guias de Despacho Electrónicas")

    @property
    def xml_enum(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.xml_enum  # o `str(obj)` si prefieres la representación de texto
        return super().default(obj)
