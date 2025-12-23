"""
vue pour récupérer un dataset par son ID
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.getDatasetByIDUseCase import GetDatasetByIDUseCase
from clean_analyze.interface.utils import standard_response
from clean_analyze.mappers.dataset_mapper import DatasetMapper

@csrf_exempt
def get_dataset_by_id(request, dataset_id):
    """
    Récupérer un dataset par son ID
    """
    if request.method != "GET":
        return standard_response(
            message="Veuillez envoyer une requête GET",
            status_str="failed",
            code=405,
            content={}
        )
    
    # dataset_id = request.GET.get("dataset_id")
    if not dataset_id:
        return standard_response(
            message="Veuillez fournir un ID de dataset",
            status_str="failed",
            code=400,
            content={}
        )
    
    try:
        dataset_id_str = str(dataset_id)  # ← maintenant c'est une vraie string
    except Exception:
        return standard_response(
            message="ID invalide",
            code=400,
            status_str="failed"
        )

    use_case = GetDatasetByIDUseCase()
    try:
        dataset = use_case.execute(dataset_id_str)
        dataset_dict = DatasetMapper.to_dict(dataset)
        return standard_response(
            message="Dataset trouvé avec succès",
            content=dataset_dict,
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