"""
vue pour récupérer le bulletin complet et classement de l'etudiant dans chque matier
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.get_student_report import GetStudentReportUseCase
from clean_analyze.interface.utils import standard_response

@csrf_exempt
def get_student_report(request, dataset_id, student_id):
    """
    Récupérer le bulletin complet et classement de l'etudiant dans chque matier
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

    if not student_id:
        return standard_response(
            message="Veuillez fournir un ID d'étudiant",
            status_str="failed"
        )

    use_case = GetStudentReportUseCase()
    try:
        stats = use_case.execute(student_id)
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