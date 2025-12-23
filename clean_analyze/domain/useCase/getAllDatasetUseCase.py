"""
recuperer toutes les dataset par id
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository

class GetAllDatasetUseCase:
    """
    Use case : récupérer tous les datasets
    """
    
    def __init__(self):
        self.repository = DjangoDatasetRepository()

    def execute(self):
        """
        Exécute la récupération de tous les datasets
        """
        return self.repository.get_all()