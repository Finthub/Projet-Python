"""
bulletin complet et classement de l'etudiant dans chque matier
"""

from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.infrastucture.analysis.panda_analysis_engine import PandaAnalysisEngine

class GetStudentReportUseCase:
    """
    bulletin complet et classement de l'etudiant dans chque matier
    """

    def __init__(self):
        self.repository = DjangoDatasetRepository()
        self.analysis_engine = PandaAnalysisEngine()

    def execute(self, student_id: str) -> dict:
        """
        Exécute la récupération du bulletin complet et classement de l'etudiant dans chque matier
        """
        dataset = self.repository.get_lastest()
        if dataset is None:
            raise ValueError("Aucun dataset trouvé")
        return self.analysis_engine.student_report(dataset.fichier_csv, student_id)