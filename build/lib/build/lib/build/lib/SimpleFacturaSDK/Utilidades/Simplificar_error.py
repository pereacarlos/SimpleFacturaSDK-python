import json

def simplificar_errores(contenido_respuesta: str) -> str:
    try:
        error_json = json.loads(contenido_respuesta)
        if "errors" in error_json:
            if isinstance(error_json["errors"], dict):
                return "; ".join(
                    f"{campo}: {', '.join(mensajes)}"
                    for campo, mensajes in error_json["errors"].items()
                )
            elif isinstance(error_json["errors"], list):
                return "; ".join(str(error) for error in error_json["errors"])
    except json.JSONDecodeError:
        return f"Error: {contenido_respuesta}"
    return contenido_respuesta
