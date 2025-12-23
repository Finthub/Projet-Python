"""
vue pour uploader les datasets
"""

from django.views.decorators.csrf import csrf_exempt

from clean_analyze.domain.useCase.upload_dataset import UploadDatasetUseCase
from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.interface.utils import standard_response
# clean_analyze/interface/api/views.py  (ou où tu veux)

@csrf_exempt
def upload_dataset(request):
    """
    Endpoint pour le téléversement de fichiers
    """
    if request.method != "POST":
        return standard_response(
            message="Méthode non autorisée. Utilisez POST.",
            code=405,
            status_str="failed"
        )

    # Vérifie qu'il y a AU MOINS un fichier, peu importe le nom du champ
    if not request.FILES:
        return standard_response(
            message="Aucun fichier détecté dans la requête",
            code=400,
            status_str="failed"
        )

    # DYNAMIQUE : prend le PREMIER fichier envoyé, quelque soit son nom
    uploaded_file = next(iter(request.FILES.values()))

    # Sécurité supplémentaire
    if not uploaded_file.name.lower().endswith('.csv'):
        return standard_response(
            message="Seul les fichiers .csv sont acceptés",
            code=400,
            status_str="failed"
        )

    try:
        # UseCase
        use_case = UploadDatasetUseCase(DjangoDatasetRepository())
        dataset = use_case.execute(
            nom_fichier=uploaded_file.name,
            chemin_csv=uploaded_file  # ← Django FileField, PAS .path ici !
        )

        return standard_response(
            message="Fichier CSV uploadé avec succès !",
            content={
                "dataset_id": str(dataset.id),
                "nom_fichier": uploaded_file.name,
                "taille_octets": uploaded_file.size,
            },
            code=201,
            status_str="succes"
        )

    except Exception as e:
        return standard_response(
            message=f"Erreur lors de l'upload : {str(e)}",
            code=500,
            status_str="failed"
        )