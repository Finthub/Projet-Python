# Guide de Démarrage Rapide - Tests API

## Prérequis

1. Python 3.12+
2. Virtual environment activé
3. Django et dépendances installées

## Installation

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Si Django REST Framework n'est pas installé (vérifier si nécessaire)
pip install djangorestframework
```

## Configuration

Les URLs de l'API sont maintenant configurées dans `analyze/urls.py` :
```python
path('api/', include('clean_analyze.interface.urls'))
```

## Démarrage du Serveur

```bash
python manage.py runserver
```

Le serveur sera accessible sur `http://localhost:8000`

## Tests Rapides

### 1. Test avec cURL

```bash
# Tester l'endpoint "Get All"
curl http://localhost:8000/api/getAll/

# Tester l'upload (remplacer le chemin du fichier)
curl -X POST http://localhost:8000/api/upload/ \
  -F "file=@/chemin/vers/votre/fichier.csv"
```

### 2. Test avec Python

```python
import requests

# Test simple
response = requests.get("http://localhost:8000/api/getAll/")
print(response.json())
```

### 3. Test avec Postman

1. Importer la collection depuis `API_DOCUMENTATION.md`
2. Configurer les variables d'environnement
3. Tester chaque endpoint

## Structure des Endpoints

Tous les endpoints sont préfixés par `/api/` :

- `/api/upload/` - Upload de fichier CSV
- `/api/getAll/` - Liste tous les datasets
- `/api/getById/<id>/` - Récupère un dataset
- `/api/globalStat/<id>/` - Statistiques globales
- `/api/departementStat/<id>/` - Stats par département
- `/api/subjectStat/<id>/<subject>/` - Stats par matière
- `/api/teacherStat/<id>/<teacher>/` - Stats par enseignant
- `/api/studentReport/<id>/<student_id>/` - Rapport étudiant
- `/api/topFlops/<id>/<category>/` - Top 10 flops
- `/api/delete/<id>/` - Supprimer un dataset

## Format CSV Attendu

Le fichier CSV doit contenir ces colonnes :
- `student_id`
- `note`
- `departement`
- `Code_ue`
- `Matiere`
- `Enseignant`

## Documentation Complète

Voir `API_DOCUMENTATION.md` pour la documentation détaillée avec tous les exemples.

