"""
structure de reponse standard pour l'API
"""
from django.http import JsonResponse

def standard_response(
    message: str = "",
    content: dict | list | None = None,
    code: int = 200,
    status_str: str = "succes"
):
    """
    Retourne une réponse standardisée pour l'API avec 'succès' ou 'échec'.

    :param message: Message à envoyer
    :param content: Données à inclure
    :param code: Code HTTP
    :param status_str: 'succes' ou 'failed'
    """
    if status_str not in ("succes", "failed"):
        raise ValueError("Le status doit être 'succes' ou 'failed'")
    
    data = {
        "status": status_str,
        "code": code,
        "message": message,
        "content": content if content is not None else {}
    }
    return JsonResponse(data, status=code)
