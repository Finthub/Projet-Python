"""
Récupérer un dataset par son ID
"""

from uuid import UUID
from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository

class GetDatasetByIDUseCase:
    """
    Use case : récupérer un dataset par son ID
    """

    def __init__(self):
        self.repository = DjangoDatasetRepository()
    
    def execute(self, dataset_id: str):
        """
        Exécute la récupération d'un dataset par son ID
        """
        dataset_uuid = UUID(dataset_id)
        dataset = self.repository.get_by_id(dataset_uuid)
        if dataset is None:
            raise ValueError(f"Dataset {dataset_id} non trouvé")
        return dataset