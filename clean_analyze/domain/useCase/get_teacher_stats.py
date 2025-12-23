"""
Récupérer les statistiques par enseignant d'un dataset
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.infrastucture.analysis.panda_analysis_engine import PandaAnalysisEngine

class GetTeacherStatsUseCase:
    """
    performance d'un enseignan
    """
    def __init__(self):
        self.repository = DjangoDatasetRepository()
        self.analysis_engine = PandaAnalysisEngine()

    def execute(self, teacher: str) -> list:
        """
        Exécute la récupération des statistiques par enseignant d'un dataset
        """
        dataset = self.repository.get_lastest()
        if dataset is None:
            raise ValueError("Aucun dataset trouvé")
        return self.analysis_engine.stats_by_teacher(dataset.fichier_csv, teacher)