"""
Entités pour le projet de nettoyage et analyse de données
"""

from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from typing import Optional

@dataclass
class DatasetEntity:
    """
    Entité pour stocker les donées des fichiers CSV
    """
    id: UUID
    nom_fichier: str
    fichier_csv: str
    data_upload: datetime
    stats_csv: Optional[str] = None
    notes_numpy: Optional[str] = None