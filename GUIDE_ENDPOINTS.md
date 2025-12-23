# Guide d'utilisation des Endpoints Subject et Teacher

## Endpoint Subject (Matière)

### Méthode 1 : Paramètres dans l'URL (avec encodage)
```
GET {{baseURL}}/api/subjectStat/<dataset_id>/<subject>/
```

### Méthode 2 : Query Parameters (recommandé pour les caractères spéciaux)
```
GET {{baseURL}}/api/subjectStat/?dataset_id=<dataset_id>&subject=<subject>
```

### Exemples

**1. Matière simple (sans espaces) :**
```
GET http://localhost:8000/api/subjectStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Programmation%20avancée/
```

**2. Matière avec espaces (encodage URL requis) :**
```
GET http://localhost:8000/api/subjectStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Réseaux%20avancés/
```

**Encodage des caractères spéciaux :**
- Espace → `%20`
- É → `%C3%89` ou `%C3%A9` (selon majuscule/minuscule)
- À → `%C3%80`
- etc.

### Exemples de matières dans le CSV :
- "Réseaux avancés"
- "Mécanique générale"
- "Programmation avancée"
- "Théorie des Signaux"
- "Machine Learning"
- "Conception logicielle"
- "Électrotechnique"
- "Calcul scientifique"

### Exemple avec cURL :
```bash
# Matière : "Programmation avancée"
curl "http://localhost:8000/api/subjectStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Programmation%20avancée/"

# Matière : "Réseaux avancés"
curl "http://localhost:8000/api/subjectStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/R%C3%A9seaux%20avanc%C3%A9s/"
```

### Exemple avec Python (requests) - Méthode 1 (URL) :
```python
import requests
from urllib.parse import quote

base_url = "http://localhost:8000/api"
dataset_id = "4c166754-e2d6-45e7-9e8b-a11d45dd4214"
subject = "Programmation avancée"  # ou "Réseaux avancés"

# Encoder le nom de la matière
subject_encoded = quote(subject)
url = f"{base_url}/subjectStat/{dataset_id}/{subject_encoded}/"

response = requests.get(url)
print(response.json())
```

### Exemple avec Python (requests) - Méthode 2 (Query Parameters - RECOMMANDÉ) :
```python
import requests

base_url = "http://localhost:8000/api"
dataset_id = "4c166754-e2d6-45e7-9e8b-a11d45dd4214"
subject = "Programmation avancée"  # ou "Réseaux avancés"

# Plus simple avec query parameters - pas besoin d'encoder manuellement
url = f"{base_url}/subjectStat/"
params = {
    "dataset_id": dataset_id,
    "subject": subject
}

response = requests.get(url, params=params)
print(response.json())
```

### Exemple avec JavaScript (fetch) :
```javascript
const baseURL = "http://localhost:8000/api";
const datasetId = "4c166754-e2d6-45e7-9e8b-a11d45dd4214";
const subject = "Programmation avancée";

// Encoder le nom de la matière
const subjectEncoded = encodeURIComponent(subject);
const url = `${baseURL}/subjectStat/${datasetId}/${subjectEncoded}/`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Endpoint Teacher (Enseignant)

### Méthode 1 : Paramètres dans l'URL (avec encodage)
```
GET {{baseURL}}/api/teacherStat/<dataset_id>/<teacher>/
```

### Méthode 2 : Query Parameters (recommandé pour les caractères spéciaux)
```
GET {{baseURL}}/api/teacherStat/?dataset_id=<dataset_id>&teacher=<teacher>
```

### Exemples

**1. Nom complet de l'enseignant :**
```
GET http://localhost:8000/api/teacherStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Pr.%20T.%20Lawson/
```

**2. Recherche partielle (recherche insensible à la casse) :**
```
GET http://localhost:8000/api/teacherStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Lawson/
```

**Encodage des caractères spéciaux :**
- Espace → `%20`
- Point → `%2E` (ou `.` fonctionne aussi généralement)
- etc.

### Exemples d'enseignants dans le CSV :
- "Pr. T. Lawson"
- "Dr. Y. Amegah"
- "Pr. D. Tchalla"
- "Pr. G. Komlan"
- "Dr. M. Kpante"
- "Dr. K. Agbeko"
- "Pr. L. Mensah"

### Exemple avec cURL :
```bash
# Enseignant complet : "Pr. T. Lawson"
curl "http://localhost:8000/api/teacherStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Pr.%20T.%20Lawson/"

# Recherche partielle : "Lawson"
curl "http://localhost:8000/api/teacherStat/4c166754-e2d6-45e8b-a11d45dd4214/Lawson/"

# Recherche partielle : "Amegah"
curl "http://localhost:8000/api/teacherStat/4c166754-e2d6-45e7-9e8b-a11d45dd4214/Amegah/"
```

### Exemple avec Python (requests) - Méthode 1 (URL) :
```python
import requests
from urllib.parse import quote

base_url = "http://localhost:8000/api"
dataset_id = "4c166754-e2d6-45e7-9e8b-a11d45dd4214"
teacher = "Pr. T. Lawson"  # ou juste "Lawson" pour recherche partielle

# Encoder le nom de l'enseignant
teacher_encoded = quote(teacher)
url = f"{base_url}/teacherStat/{dataset_id}/{teacher_encoded}/"

response = requests.get(url)
print(response.json())
```

### Exemple avec Python (requests) - Méthode 2 (Query Parameters - RECOMMANDÉ) :
```python
import requests

base_url = "http://localhost:8000/api"
dataset_id = "4c166754-e2d6-45e7-9e8b-a11d45dd4214"
teacher = "Pr. T. Lawson"  # ou "Lawson" pour recherche partielle

# Plus simple avec query parameters - pas besoin d'encoder manuellement
url = f"{base_url}/teacherStat/"
params = {
    "dataset_id": dataset_id,
    "teacher": teacher
}

response = requests.get(url, params=params)
print(response.json())
```

### Exemple avec JavaScript (fetch) :
```javascript
const baseURL = "http://localhost:8000/api";
const datasetId = "4c166754-e2d6-45e7-9e8b-a11d45dd4214";
const teacher = "Pr. T. Lawson"; // ou "Lawson" pour recherche partielle

// Encoder le nom de l'enseignant
const teacherEncoded = encodeURIComponent(teacher);
const url = `${baseURL}/teacherStat/${datasetId}/${teacherEncoded}/`;

fetch(url)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Notes importantes

1. **Deux méthodes disponibles** :
   - **Méthode 1 (URL)** : Paramètres dans l'URL, nécessite l'encodage manuel des caractères spéciaux
   - **Méthode 2 (Query Parameters)** : ⭐ **RECOMMANDÉ** - Plus simple, pas besoin d'encoder manuellement

2. **Recherche partielle pour teacher** : L'endpoint teacher utilise `str.contains()`, donc vous pouvez rechercher par partie du nom (ex: "Lawson" au lieu de "Pr. T. Lawson")

3. **Recherche exacte pour subject** : L'endpoint subject utilise une comparaison exacte, donc le nom doit correspondre exactement au nom dans le CSV

4. **Exemples de noms dans le CSV** :
   - **Matières** : "Réseaux avancés", "Mécanique générale", "Programmation avancée", etc.
   - **Enseignants** : "Pr. T. Lawson", "Dr. Y. Amegah", "Pr. D. Tchalla", etc.

## Outils pour encoder les URLs

- **Python** : `urllib.parse.quote()` ou `urllib.parse.quote_plus()`
- **JavaScript** : `encodeURIComponent()`
- **En ligne** : https://www.urlencoder.org/

## Exemples de réponses

### Subject Response :
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": {
        "matiere": "Programmation avancée",
        "moyenne": 15.5,
        "total_etudiants": 45,
        "total_notes": 45,
        "taux_reussite_%": 72.5,
        "boxplot_data": [8, 10, 12, 14, 16, ...],
        "departement": ["Informatique"],
        "code_ue": ["CS220"],
        "mediane": 15.0,
        "ecart_type": 2.8,
        "histogramme": [2, 5, 8, ...],
        "bins": [0.0, 1.0, 2.0, ...]
    }
}
```

### Teacher Response :
```json
{
    "status": "succes",
    "code": 200,
    "message": "Statistiques trouvées avec succès",
    "content": [
        {
            "intitulé_matière": "Réseaux avancés",
            "moyenne": 13.5,
            "nb_etudiants": 45
        },
        {
            "intitulé_matière": "Conception logicielle",
            "moyenne": 14.2,
            "nb_etudiants": 42
        }
    ]
}
```

