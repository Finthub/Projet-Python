"""
vue pour récupérer les statistiques par enseignant d'un dataset
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.get_teacher_stats import GetTeacherStatsUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def get_teacher_stats(request, dataset_id=None, teacher=None):
    """
    Récupérer les statistiques par enseignant d'un dataset
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

    # Récupérer teacher depuis l'URL ou query parameter
    teacher = teacher or request.GET.get("teacher")

    if not teacher:
        return standard_response(
            message="Veuillez fournir un enseignant",
            status_str="failed"
        )

    use_case = GetTeacherStatsUseCase()
    try:
        stats = use_case.execute(teacher)
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