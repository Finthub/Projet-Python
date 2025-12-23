"""
supprimer un dataset
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
class DeleteDatasetUseCase:
    """
    Use case : supprimer un dataset
    """
    
    def __init__(self):
        self.dataset_repository = DjangoDatasetRepository()

    def execute(self, dataset_id: str) -> None:
        """
        Exécute la suppression d'un dataset
        """
        self.dataset_repository.delete(dataset_id)