"""
Récupérer les top 10 flops(matiere ou enseignant les plus facile)
"""
from clean_analyze.infrastucture.repositories.dataset_repo import DjangoDatasetRepository
from clean_analyze.infrastucture.analysis.panda_analysis_engine import PandaAnalysisEngine

class GetTopFlopsUseCase:
    """ 
    top 10 flops(matiere ou enseignant les plus facile)
    """

    def __init__(self):
        self.repository = DjangoDatasetRepository()
        self.analysis_engine = PandaAnalysisEngine()

    def execute(self, category: str = "matiere") -> dict:
        """
        Exécute la récupération des statistiques par département d'un dataset
        """
        dataset = self.repository.get_lastest()
        if dataset is None:
            raise ValueError("Aucun dataset trouvé")
        return self.analysis_engine.top_flops(dataset.fichier_csv, category)