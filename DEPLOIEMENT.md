# Guide de Déploiement Docker - Projet Django Analyze

## Fichiers créés

- **dockerfile** : Configuration Docker pour construire l'image
- **docker-compose.yml** : Orchestration des services Docker
- **.dockerignore** : Fichiers à exclure lors du build Docker

## Déploiement en Local

### 1. Construction et lancement avec Docker Compose

```bash
# Construire et lancer le conteneur
docker-compose up --build

# Ou en arrière-plan
docker-compose up -d --build
```

L'application sera accessible sur `http://localhost:8000`

### 2. Commandes utiles

```bash
# Arrêter les conteneurs
docker-compose down

# Voir les logs
docker-compose logs -f

# Redémarrer les conteneurs
docker-compose restart

# Exécuter des commandes Django dans le conteneur
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## Déploiement sur un Serveur

### Option 1 : Déploiement VPS (DigitalOcean, AWS EC2, etc.)

#### Prérequis sur le serveur
```bash
# Installer Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Installer Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Déploiement
```bash
# 1. Se connecter au serveur
ssh user@votre-serveur.com

# 2. Cloner le projet
git clone <votre-repo-git>
cd Projet-Python

# 3. Créer un fichier .env (optionnel mais recommandé)
nano .env
# Ajouter:
# DEBUG=False
# SECRET_KEY=votre-cle-secrete-generee
# ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com

# 4. Modifier docker-compose.yml pour la production
# Remplacer SECRET_KEY par une clé sécurisée
# Configurer ALLOWED_HOSTS avec votre domaine

# 5. Lancer l'application
docker-compose up -d --build

# 6. Vérifier que tout fonctionne
docker-compose ps
docker-compose logs
```

### Option 2 : Utiliser Docker Hub

#### 1. Créer et pousser l'image sur Docker Hub
```bash
# Se connecter à Docker Hub
docker login

# Construire l'image
docker build -t votre-username/django-analyze:latest .

# Pousser l'image
docker push votre-username/django-analyze:latest
```

#### 2. Sur le serveur
```bash
# Récupérer l'image
docker pull votre-username/django-analyze:latest

# Lancer le conteneur
docker run -d -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY=votre-cle-secrete \
  -e ALLOWED_HOSTS=votre-domaine.com \
  --name django-app \
  votre-username/django-analyze:latest
```

### Option 3 : Avec Nginx en reverse proxy (Production recommandée)

Créer un fichier `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: django-analyze-app
    expose:
      - "8000"
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    environment:
      - DEBUG=False
      - DJANGO_SETTINGS_MODULE=analyze.settings
      - SECRET_KEY=${SECRET_KEY}
      - ALLOWED_HOSTS=${ALLOWED_HOSTS}
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web
    restart: unless-stopped

volumes:
  static_volume:
  media_volume:
```

## Configuration de Production Importante

### 1. Modifier `analyze/settings.py`

Ajouter à la fin du fichier:

```python
import os

# Production settings
if not DEBUG:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
    SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

    # Static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Security settings
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

### 2. Générer une SECRET_KEY sécurisée

```python
# Dans un terminal Python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Ports et Accès

- **Port 8000** : Application Django
- Assurez-vous que le port 8000 est ouvert sur votre firewall

```bash
# Sur Ubuntu/Debian
sudo ufw allow 8000
sudo ufw enable
```

## Surveillance et Logs

```bash
# Voir les logs en temps réel
docker-compose logs -f web

# Voir les dernières 100 lignes
docker-compose logs --tail=100 web

# Statistiques d'utilisation
docker stats
```

## Backup de la base de données

```bash
# Copier la base de données hors du conteneur
docker-compose exec web python manage.py dumpdata > backup.json

# Ou copier le fichier SQLite directement
docker cp django-analyze-app:/app/db.sqlite3 ./backup.sqlite3
```

## Mise à jour de l'application

```bash
# 1. Récupérer les dernières modifications
git pull

# 2. Reconstruire et redémarrer
docker-compose down
docker-compose up -d --build

# 3. Appliquer les migrations si nécessaire
docker-compose exec web python manage.py migrate
```

## Dépannage

### L'application ne démarre pas
```bash
# Vérifier les logs
docker-compose logs web

# Vérifier que le port n'est pas déjà utilisé
sudo netstat -tuln | grep 8000
```

### Problème de permissions
```bash
# Reconstruire sans cache
docker-compose build --no-cache
docker-compose up -d
```

### Base de données corrompue
```bash
# Supprimer et recréer
docker-compose down
rm db.sqlite3
docker-compose up -d
docker-compose exec web python manage.py migrate
```

## Services Cloud recommandés

1. **DigitalOcean** : Simple droplet à partir de 5$/mois
2. **AWS EC2** : Instance t2.micro (gratuit la première année)
3. **Heroku** : Déploiement facile (nécessite configuration supplémentaire)
4. **Railway** : Déploiement depuis GitHub très simple
5. **Render** : Alternative à Heroku avec plan gratuit

## Sécurité - Checklist Production

- [ ] Changer SECRET_KEY
- [ ] Mettre DEBUG=False
- [ ] Configurer ALLOWED_HOSTS
- [ ] Utiliser HTTPS (Certbot/Let's Encrypt)
- [ ] Configurer un pare-feu
- [ ] Utiliser des variables d'environnement pour les secrets
- [ ] Activer les headers de sécurité Django
- [ ] Mettre en place des sauvegardes automatiques
- [ ] Configurer la surveillance (uptime monitoring)
