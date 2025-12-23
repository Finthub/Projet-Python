"""
Récupérer les statistiques globales d'un dataset
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.infrastucture.analysis.panda_analysis_engine import PandaAnalysisEngine

class GetGlobalStatsUseCase:
    """
    statistitics generales d'un dataset:
        - moyenne
        - mediane
        - ecart type
        - taux de réussite
        - histogramme
        - bins
    """
    
    def __init__(self):
        self.repository = DjangoDatasetRepository()
        self.analysis_engine = PandaAnalysisEngine()

    def execute(self, dataset_id: str) -> dict:
        """
        Exécute la récupération des statistiques globales d'un dataset
        """
        dataset = self.repository.get_by_id(dataset_id)
        if dataset is None:
            raise ValueError(f"Dataset {dataset_id} non trouvé")
        return self.analysis_engine.global_stats(dataset.fichier_csv)
