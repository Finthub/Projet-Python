# Documentation API - Tableau de Bord Statistiques

Cette documentation décrit tous les endpoints disponibles pour tester l'API de gestion et d'analyse de datasets.

## Configuration

**Base URL**: `http://localhost:8000/api/` (ou votre URL de serveur)

**Format de réponse standard**:
```json
{
    "status": "succes" | "failed",
    "code": 200,
    "message": "Message descriptif",
    "content": {} | []
}
```

---

## 1. Upload d'un Dataset

**Endpoint**: `POST /api/upload/`

**Description**: Upload un fichier CSV et le sauvegarde dans le système.

**Paramètres**:
- `file` (form-data, fichier CSV): Le fichier CSV à uploader

**Exemple avec cURL**:
```bash
curl -X POST http://localhost:8000/api/upload/ \
  -F "file=@/chemin/vers/votre/fichier.csv"
```

**Exemple avec Python (requests)**:
```python
import requests

url = "http://localhost:8000/api/upload/"
files = {'file': open('votre_fichier.csv', 'rb')}

response = requests.post(url, files=files)
print(response.json())
```

**Réponse succès (201)**:
```json
{
    "status": "succes",
    "code": 201,
    "message": "Fichier uploadé avec succès",
    "content": {
        "dataset_id": "550e8400-e29b-41d4-a716-446655440000"
    }
}
```

**Réponse erreur (400)**:
```json
{
    "status": "failed",
    "code": 400,
    "message": "Veuillez envoyer un fichier CSV",
    "content": {}
}
```

---

## 2. Récupérer tous les Datasets

**Endpoint**: `GET /api/getAll/`

**Description**: Récupère la liste de tous les datasets uploadés.

**Exemple avec cURL**:
```bash
curl -X GET http://localhost:8000/api/getAll/
```

**Exemple avec Python**:
```python
import requests

url = "http://localhost:8000/api/getAll/"
response = requests.get(url)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Tous les datasets trouvés avec succès",
    "content": [
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "nom_fichier": "notes_2024.csv",
            "date_upload": "2024-01-15T10:30:00Z"
        }
    ]
}
```

---

## 3. Récupérer un Dataset par ID

**Endpoint**: `GET /api/getById/<dataset_id>/`

**Description**: Récupère les informations d'un dataset spécifique par son ID.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset

**Paramètres Query** (alternative):
- `dataset_id` (query parameter): L'identifiant unique du dataset

**Exemple avec cURL**:
```bash
# Méthode 1: Paramètre dans l'URL
curl -X GET "http://localhost:8000/api/getById/550e8400-e29b-41d4-a716-446655440000/"

# Méthode 2: Query parameter
curl -X GET "http://localhost:8000/api/getById/?dataset_id=550e8400-e29b-41d4-a716-446655440000"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
url = f"http://localhost:8000/api/getById/{dataset_id}/"
# ou
url = "http://localhost:8000/api/getById/"
params = {"dataset_id": dataset_id}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Dataset trouvé avec succès",
    "content": {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "nom_fichier": "notes_2024.csv",
        "fichier_csv": "/chemin/vers/fichier.csv",
        "date_upload": "2024-01-15T10:30:00Z"
    }
}
```

---

## 4. Statistiques Globales

**Endpoint**: `GET /api/globalStat/<dataset_id>/`

**Description**: Récupère les statistiques globales d'un dataset (moyenne, médiane, écart-type, taux de réussite, histogramme).

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset

**Exemple avec cURL**:
```bash
curl -X GET "http://localhost:8000/api/globalStat/550e8400-e29b-41d4-a716-446655440000/?dataset_id=550e8400-e29b-41d4-a716-446655440000"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
url = f"http://localhost:8000/api/globalStat/{dataset_id}/"
params = {"dataset_id": dataset_id}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": {
        "total_etudiants": 150,
        "total_notes": 1200,
        "moyenne": 12.5,
        "mediane": 12.0,
        "ecart_type": 3.2,
        "taux_reussite_%": 65.5,
        "histogramme": [10, 15, 20, ...],
        "bins": [0.0, 1.0, 2.0, ...]
    }
}
```

---

## 5. Statistiques par Département

**Endpoint**: `GET /api/departementStat/<dataset_id>/`

**Description**: Récupère les statistiques groupées par département, UE et matière.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset

**Exemple avec cURL**:
```bash
curl -X GET "http://localhost:8000/api/departementStat/550e8400-e29b-41d4-a716-446655440000/?dataset_id=550e8400-e29b-41d4-a716-446655440000"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
url = f"http://localhost:8000/api/departementStat/{dataset_id}/"
params = {"dataset_id": dataset_id}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": [
        {
            "departement": "Informatique",
            "Code_ue": "UE101",
            "Matiere": "Algorithmes",
            "moyenne": 13.5,
            "mediane": 13.0,
            "ecart_type": 2.8,
            "nb_etudiants": 45,
            "taux_reussite": 72.5,
            "count": 45
        }
    ]
}
```

---

## 6. Statistiques par Matière

**Endpoint**: `GET /api/subjectStat/<dataset_id>/<subject>/`

**Description**: Récupère les statistiques détaillées pour une matière spécifique.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset
- `subject` (string): Le nom de la matière

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset
- `subject` (query parameter): Le nom de la matière

**Exemple avec cURL**:
```bash
curl -X GET "http://localhost:8000/api/subjectStat/550e8400-e29b-41d4-a716-446655440000/Algorithmes/?dataset_id=550e8400-e29b-41d4-a716-446655440000&subject=Algorithmes"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
subject = "Algorithmes"
url = f"http://localhost:8000/api/subjectStat/{dataset_id}/{subject}/"
params = {
    "dataset_id": dataset_id,
    "subject": subject
}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": {
        "matiere": "Algorithmes",
        "moyenne": 13.5,
        "total_etudiants": 45,
        "total_notes": 45,
        "taux_reussite_%": 72.5,
        "boxplot_data": [8, 10, 12, 14, 16, ...],
        "departement": ["Informatique"],
        "code_ue": ["UE101"],
        "mediane": 13.0,
        "ecart_type": 2.8,
        "histogramme": [2, 5, 8, ...],
        "bins": [0.0, 1.0, 2.0, ...]
    }
}
```

---

## 7. Statistiques par Enseignant

**Endpoint**: `GET /api/teacherStat/<dataset_id>/<teacher>/`

**Description**: Récupère les statistiques pour un enseignant spécifique.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset
- `teacher` (string): Le nom de l'enseignant (recherche partielle)

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset
- `teacher` (query parameter): Le nom de l'enseignant

**Exemple avec cURL**:
```bash
curl -X GET "http://localhost:8000/api/teacherStat/550e8400-e29b-41d4-a716-446655440000/Dupont/?dataset_id=550e8400-e29b-41d4-a716-446655440000&teacher=Dupont"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
teacher = "Dupont"
url = f"http://localhost:8000/api/teacherStat/{dataset_id}/{teacher}/"
params = {
    "dataset_id": dataset_id,
    "teacher": teacher
}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": [
        {
            "Matière": "Algorithmes",
            "moyenne": 13.5,
            "nb_etudiants": 45
        },
        {
            "Matière": "Structures de données",
            "moyenne": 14.2,
            "nb_etudiants": 42
        }
    ]
}
```

---

## 8. Rapport Étudiant

**Endpoint**: `GET /api/studentReport/<dataset_id>/<student_id>/`

**Description**: Récupère le bulletin complet d'un étudiant avec son classement dans chaque matière.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset
- `student_id` (string): L'identifiant de l'étudiant

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset
- `student_id` (query parameter): L'identifiant de l'étudiant

**Exemple avec cURL**:
```bash
curl -X GET "http://localhost:8000/api/studentReport/550e8400-e29b-41d4-a716-446655440000/STU001/?dataset_id=550e8400-e29b-41d4-a716-446655440000&student_id=STU001"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
student_id = "STU001"
url = f"http://localhost:8000/api/studentReport/{dataset_id}/{student_id}/"
params = {
    "dataset_id": dataset_id,
    "student_id": student_id
}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": {
        "etudiant_id": "STU001",
        "moyenne": 13.5,
        "credits_reussis": 8,
        "bulletin": {
            "Algorithmes": {
                "Dupont": 14.5
            },
            "Structures de données": {
                "Martin": 12.0
            }
        },
        "classements": [
            {
                "matiere": "Algorithmes",
                "note": 14.5,
                "classement": "15e / 45"
            },
            {
                "matiere": "Structures de données",
                "note": 12.0,
                "classement": "28e / 42"
            }
        ]
    }
}
```

---

## 9. Top 10 Flops

**Endpoint**: `GET /api/topFlops/<dataset_id>/<category>/`

**Description**: Récupère les top 10 matières ou enseignants avec les meilleures moyennes (les plus "faciles").

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset
- `category` (string): `"matiere"` ou `"enseignant"`

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset
- `category` (query parameter): `"matiere"` ou `"enseignant"`

**Exemple avec cURL**:
```bash
# Top 10 matières
curl -X GET "http://localhost:8000/api/topFlops/550e8400-e29b-41d4-a716-446655440000/matiere/?dataset_id=550e8400-e29b-41d4-a716-446655440000&category=matiere"

# Top 10 enseignants
curl -X GET "http://localhost:8000/api/topFlops/550e8400-e29b-41d4-a716-446655440000/enseignant/?dataset_id=550e8400-e29b-41d4-a716-446655440000&category=enseignant"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
category = "matiere"  # ou "enseignant"
url = f"http://localhost:8000/api/topFlops/{dataset_id}/{category}/"
params = {
    "dataset_id": dataset_id,
    "category": category
}

response = requests.get(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": {
        "Algorithmes": 16.5,
        "Base de données": 15.8,
        "Réseaux": 15.2,
        ...
    }
}
```

---

## 10. Supprimer un Dataset

**Endpoint**: `DELETE /api/delete/<dataset_id>/`

**Description**: Supprime un dataset et tous ses fichiers associés.

**Paramètres URL**:
- `dataset_id` (string, UUID): L'identifiant unique du dataset

**Paramètres Query**:
- `dataset_id` (query parameter): L'identifiant unique du dataset

**Exemple avec cURL**:
```bash
curl -X DELETE "http://localhost:8000/api/delete/550e8400-e29b-41d4-a716-446655440000/?dataset_id=550e8400-e29b-41d4-a716-446655440000"
```

**Exemple avec Python**:
```python
import requests

dataset_id = "550e8400-e29b-41d4-a716-446655440000"
url = f"http://localhost:8000/api/delete/{dataset_id}/"
params = {"dataset_id": dataset_id}

response = requests.delete(url, params=params)
print(response.json())
```

**Réponse succès (200)**:
```json
{
    "status": "succes",
    "code": 200,
    "message": "Dataset supprimé avec succès",
    "content": {}
}
```

---

## Format du Fichier CSV Attendu

Le fichier CSV uploadé doit contenir les colonnes suivantes :
- `student_id` : Identifiant de l'étudiant
- `note` : Note obtenue (nombre)
- `departement` : Nom du département
- `Code_ue` : Code de l'UE
- `Matiere` : Nom de la matière
- `Enseignant` : Nom de l'enseignant

**Exemple de CSV**:
```csv
student_id,note,departement,Code_ue,Matiere,Enseignant
STU001,14.5,Informatique,UE101,Algorithmes,Dupont
STU002,12.0,Informatique,UE101,Algorithmes,Dupont
STU003,16.0,Informatique,UE102,Structures de données,Martin
```

---

## Codes d'Erreur

- **200** : Succès
- **201** : Créé avec succès (upload)
- **400** : Requête invalide (paramètres manquants)
- **404** : Ressource non trouvée
- **500** : Erreur serveur

---

## Notes Importantes

1. **CSRF Exempt** : Tous les endpoints sont exemptés de CSRF pour faciliter les tests. En production, il faudra gérer cela différemment.

2. **Format UUID** : Les `dataset_id` doivent être au format UUID (ex: `550e8400-e29b-41d4-a716-446655440000`).

3. **Paramètres** : Certains endpoints acceptent les paramètres soit dans l'URL soit en query parameters. Utilisez la méthode qui vous convient le mieux.

4. **Démarrage du serveur** : Assurez-vous que le serveur Django est démarré :
   ```bash
   python manage.py runserver
   ```

5. **Inclusion des URLs** : Avant de tester, assurez-vous que les URLs de `clean_analyze` sont incluses dans le fichier `analyze/urls.py` :
   ```python
   from django.urls import include, path
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('clean_analyze.interface.urls')),
   ]
   ```

---

## Script de Test Complet (Python)

Voici un script Python complet pour tester tous les endpoints :

```python
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_upload():
    """Test l'upload d'un fichier CSV"""
    url = f"{BASE_URL}/upload/"
    files = {'file': open('test_data.csv', 'rb')}
    response = requests.post(url, files=files)
    print("Upload:", response.json())
    return response.json()['content']['dataset_id']

def test_get_all():
    """Test la récupération de tous les datasets"""
    url = f"{BASE_URL}/getAll/"
    response = requests.get(url)
    print("Get All:", response.json())

def test_get_by_id(dataset_id):
    """Test la récupération d'un dataset par ID"""
    url = f"{BASE_URL}/getById/{dataset_id}/"
    params = {"dataset_id": dataset_id}
    response = requests.get(url, params=params)
    print("Get By ID:", response.json())

def test_global_stats(dataset_id):
    """Test les statistiques globales"""
    url = f"{BASE_URL}/globalStat/{dataset_id}/"
    params = {"dataset_id": dataset_id}
    response = requests.get(url, params=params)
    print("Global Stats:", response.json())

def test_department_stats(dataset_id):
    """Test les statistiques par département"""
    url = f"{BASE_URL}/departementStat/{dataset_id}/"
    params = {"dataset_id": dataset_id}
    response = requests.get(url, params=params)
    print("Department Stats:", response.json())

def test_subject_stats(dataset_id, subject):
    """Test les statistiques par matière"""
    url = f"{BASE_URL}/subjectStat/{dataset_id}/{subject}/"
    params = {"dataset_id": dataset_id, "subject": subject}
    response = requests.get(url, params=params)
    print("Subject Stats:", response.json())

def test_teacher_stats(dataset_id, teacher):
    """Test les statistiques par enseignant"""
    url = f"{BASE_URL}/teacherStat/{dataset_id}/{teacher}/"
    params = {"dataset_id": dataset_id, "teacher": teacher}
    response = requests.get(url, params=params)
    print("Teacher Stats:", response.json())

def test_student_report(dataset_id, student_id):
    """Test le rapport étudiant"""
    url = f"{BASE_URL}/studentReport/{dataset_id}/{student_id}/"
    params = {"dataset_id": dataset_id, "student_id": student_id}
    response = requests.get(url, params=params)
    print("Student Report:", response.json())

def test_top_flops(dataset_id, category):
    """Test les top flops"""
    url = f"{BASE_URL}/topFlops/{dataset_id}/{category}/"
    params = {"dataset_id": dataset_id, "category": category}
    response = requests.get(url, params=params)
    print("Top Flops:", response.json())

def test_delete(dataset_id):
    """Test la suppression d'un dataset"""
    url = f"{BASE_URL}/delete/{dataset_id}/"
    params = {"dataset_id": dataset_id}
    response = requests.delete(url, params=params)
    print("Delete:", response.json())

# Exemple d'utilisation
if __name__ == "__main__":
    # 1. Upload un fichier
    dataset_id = test_upload()
    
    # 2. Récupérer tous les datasets
    test_get_all()
    
    # 3. Récupérer un dataset par ID
    test_get_by_id(dataset_id)
    
    # 4. Statistiques globales
    test_global_stats(dataset_id)
    
    # 5. Statistiques par département
    test_department_stats(dataset_id)
    
    # 6. Statistiques par matière
    test_subject_stats(dataset_id, "Algorithmes")
    
    # 7. Statistiques par enseignant
    test_teacher_stats(dataset_id, "Dupont")
    
    # 8. Rapport étudiant
    test_student_report(dataset_id, "STU001")
    
    # 9. Top flops
    test_top_flops(dataset_id, "matiere")
    
    # 10. Supprimer le dataset (optionnel)
    # test_delete(dataset_id)
```

---

## Collection Postman

Pour importer dans Postman, créez une collection avec les requêtes suivantes :

1. **Upload Dataset** - POST `{{base_url}}/upload/` (Body: form-data, key: `file`, type: File)
2. **Get All Datasets** - GET `{{base_url}}/getAll/`
3. **Get Dataset By ID** - GET `{{base_url}}/getById/{{dataset_id}}/`
4. **Global Stats** - GET `{{base_url}}/globalStat/{{dataset_id}}/`
5. **Department Stats** - GET `{{base_url}}/departementStat/{{dataset_id}}/`
6. **Subject Stats** - GET `{{base_url}}/subjectStat/{{dataset_id}}/{{subject}}/`
7. **Teacher Stats** - GET `{{base_url}}/teacherStat/{{dataset_id}}/{{teacher}}/`
8. **Student Report** - GET `{{base_url}}/studentReport/{{dataset_id}}/{{student_id}}/`
9. **Top Flops** - GET `{{base_url}}/topFlops/{{dataset_id}}/{{category}}/`
10. **Delete Dataset** - DELETE `{{base_url}}/delete/{{dataset_id}}/`

**Variables d'environnement Postman** :
- `base_url`: `http://localhost:8000/api`
- `dataset_id`: `550e8400-e29b-41d4-a716-446655440000` (à remplacer après upload)
- `subject`: `Algorithmes`
- `teacher`: `Dupont`
- `student_id`: `STU001`
- `category`: `matiere` ou `enseignant`

