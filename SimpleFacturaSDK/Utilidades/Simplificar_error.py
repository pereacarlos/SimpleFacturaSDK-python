import json

def simplificar_errores(contenido_respuesta: str) -> str:
    try:
        error_json = json.loads(contenido_respuesta)
        if "errors" in error_json:
            return "; ".join(
                f"{campo}: {', '.join(mensajes)}"
                for campo, mensajes in error_json["errors"].items()
            )
    except json.JSONDecodeError:
        pass
    return contenido_respuesta
