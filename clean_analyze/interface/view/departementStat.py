"""
vue pour récupérer les statistiques par département d'un dataset
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.get_department_stats import GetDepartmentStatsUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def get_department_stats(request, dataset_id):
    """
    Récupérer les statistiques par département d'un dataset
    """
    if request.method != "GET":
        return standard_response(
            message="Veuillez envoyer une requête GET",
            status_str="failed"
        )
    
    # dataset_id = request.GET.get("dataset_id")
    if not dataset_id:
        return standard_response(
            message="Veuillez fournir un ID de dataset",
            status_str="failed"
        )

    use_case = GetDepartmentStatsUseCase()
    try:
        stats = use_case.execute()
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