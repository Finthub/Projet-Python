"""
vue pour supprimer un dataset
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.delete_dataset import DeleteDatasetUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def delete_dataset(request):
    """
    Supprimer un dataset
    """
    if request.method != "DELETE":
        return standard_response(
            message="Veuillez envoyer une requête DELETE",
            status_str="failed"
        )
    
    dataset_id = request.GET.get("dataset_id")
    if not dataset_id:
        return standard_response(
            message="Veuillez fournir un ID de dataset",
            status_str="failed"
        )

    use_case = DeleteDatasetUseCase()
    try:
        use_case.execute(dataset_id)
        return standard_response(
            message="Dataset supprimé avec succès",
            content={},
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