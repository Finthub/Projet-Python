"""
Récupérer les statistiques par matière d'un dataset
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.infrastucture.analysis.panda_analysis_engine import PandaAnalysisEngine

class GetSubjectStatsUseCase:
    """
    stats par matiere d'une us/ matiere
    """

    def __init__(self):
        self.repository = DjangoDatasetRepository()
        self.analysis_engine = PandaAnalysisEngine()

    def execute(self, subject: str) -> dict:
        """
        Exécute la récupération des statistiques par matiere d'un dataset
        """
        dataset = self.repository.get_lastest()
        if dataset is None:
            raise ValueError("Aucun dataset trouvé")
        return self.analysis_engine.stats_by_matiere(dataset.fichier_csv, subject)