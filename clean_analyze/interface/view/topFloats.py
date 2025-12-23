"""
vue pour récupérer les top 10 flops(matiere ou enseignant les plus facile)
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.get_top_flops import GetTopFlopsUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def get_top_flops(request, dataset_id, category):
    """
    Récupérer les top 10 flops(matiere ou enseignant les plus facile)
    """
    if request.method != "GET":
        return standard_response(
            message="Veuillez envoyer une requête GET",
            status_str="failed"
        )
    
    if not dataset_id:
        return standard_response(
            message="Veuillez fournir un ID de dataset",
            status_str="failed"
        )

    if not category:
        return standard_response(
            message="Veuillez fournir une catégorie",
            status_str="failed"
        )

    use_case = GetTopFlopsUseCase()
    try:
        stats = use_case.execute(category)
        return standard_response(
            message="Statistiques trouvées avec succès",
            content=stats,
            code=200,
            status_str="succes"
        )
    except Exception as e:
        return standard_response(
            message=str(e),
            content={},
            status_str="failed",
            code=500
        )