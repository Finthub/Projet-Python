"""
vue pour récupérer les statistiques par matière d'un dataset
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.get_subject_stats import GetSubjectStatsUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def get_subject_stats(request, dataset_id=None, subject=None):
    """
    Récupérer les statistiques par matière d'un dataset
    Supporte les paramètres dans l'URL ou en query parameters
    """
    if request.method != "GET":
        return standard_response(
            message="Veuillez envoyer une requête GET",
            status_str="failed"
        )
    
    # Récupérer dataset_id depuis l'URL ou query parameter
    dataset_id = dataset_id or request.GET.get("dataset_id")
    
    if not dataset_id:
        return standard_response(
            message="Veuillez fournir un ID de dataset",
            status_str="failed"
        )

    # Récupérer subject depuis l'URL ou query parameter
    subject = subject or request.GET.get("subject")

    if not subject:
        return standard_response(
            message="Veuillez fournir un sujet",
            status_str="failed"
        )

    use_case = GetSubjectStatsUseCase()
    try:
        stats = use_case.execute(subject)
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