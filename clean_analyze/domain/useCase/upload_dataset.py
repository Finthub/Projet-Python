"""
configuration du projet de nettoyage et analyse de données
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.domain.entities.dataset_entity import DatasetEntity  # ← ton entité pure

class UploadDatasetUseCase:
    """
    Use case : uploader un fichier CSV et le sauvegarder dans le système.
    Ce use case ne fait QUE créer le Dataset en base + sauvegarder le fichier.
    Il ne fait PAS d'analyse ici (l'analyse se fait dans un autre use case séparé).
    """
    
    def __init__(self, dataset_repository: DjangoDatasetRepository):
        self.dataset_repository = dataset_repository

    def execute(self, nom_fichier: str, chemin_csv: str) -> DatasetEntity:
        """
        Exécute l'upload du fichier CSV.
        Retourne l'entité Dataset créée (pure, sans Django dedans).
        """
        # On délègue tout au repository → le domaine reste pur
        dataset_entity = self.dataset_repository.create_and_save(nom_fichier, chemin_csv)
        return dataset_entity