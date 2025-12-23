"""
Repository pour le projet de nettoyage et analyse de données
"""

from uuid import UUID
from typing import Optional

from clean_analyze.domain.entities.dataset_entity import DatasetEntity
from clean_analyze.models import Dataset
from clean_analyze.mappers.dataset_mapper import DatasetMapper

class DjangoDatasetRepository:
    """
    repository django pour communiquer  avec la base de donnee
    """

    def create_and_save(self, nom_fichier: str, chemin_csv: str) -> DatasetEntity:
        """
        creer un nouveau dataset lors du upload
        """

        model = Dataset.objects.create(
            nom_fichier=nom_fichier,
            fichier_csv=chemin_csv
        )

        return DatasetMapper.to_entity(model)

    def get_by_id(self, dataset_id: UUID) -> Optional[DatasetEntity]:
        """
        recuperer un dataset par son ID
        """

        model = Dataset.objects.get(id=dataset_id)
        return DatasetMapper.to_entity(model)

    def get_all(self) -> list[DatasetEntity]:
        """
        recuperer tous les datasets
        """
        models = Dataset.objects.all()
        return [DatasetMapper.to_entity(model) for model in models]
    
    def get_lastest(self) -> Optional[DatasetEntity]:
        """
        Recuperer le dernier dataset uploadé
        """
        try:
            model = Dataset.objects.latest('data_upload')
            return DatasetMapper.to_entity(model)
        except Dataset.DoesNotExist:
            return None
        
    def save_analysis_results(self, dataset_id:UUID, chemin_stats: str, chemin_numpy: str) -> None:
        """
        Met a jour le dataset avec les resultat d'analyse
        """
        model = Dataset.objects.get(id=dataset_id)
        model.stats_csv = chemin_stats
        model.notes_numpy = chemin_numpy
        model.save()

    
    def delete(self, dataset_id:UUID) -> None:
        """
        supprimer completement le dtaset et ses fichiers
        """
        model = Dataset.objects.get(id=dataset_id)
        model.fichier_csv.delete()
        if model.stats_csv:
            model.stats_csv.delete()
        if model.notes_numpy:
            model.notes_numpy.delete()
        model.delete()