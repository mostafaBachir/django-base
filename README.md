# 🧱 djbase – Django Starter Template

Un socle robuste pour projets Django avec :

- 🔐 Authentification JWT (email + mot de passe)
- 🧑‍💼 Utilisateur personnalisé (`UserAccount`)
- 🧵 Tâches asynchrones avec Celery + django-celery-beat
- 📡 WebSocket temps réel (Django Channels + Redis)
- 🪵 Visualisation des logs via API + WebSocket
- ⚙️ Configuration modulaire (`base.py`, `dev.py`, `prod.py`)

---

## 🚀 Démarrage rapide

### 1. Cloner le projet et créer l'environnement

```bash
git clone https://github.com/votre-utilisateur/djbase.git
cd djbase
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Configuration .env
Créer un fichier .env à la racine :


SECRET_KEY=...
JWT_SECRET=...
DEBUG=True

DATABASE_URL=postgres://user:password@localhost:11002/mydb
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

🧩 Structure

djbase/
├── config/              # Settings, ASGI, Celery
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── routing.py       # WebSocket routes
│   ├── celery.py
│   └── asgi.py
├── accounts/            # Authentification & User
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── serializers.py
│   └── urls.py
├── logs/                # Logs API + WebSocket
│   ├── views.py
│   ├── consumers.py
│   └── urls.py
├── requirements.txt
└── python_version.txt


🧠 Authentification JWT
POST /api/accounts/register/ : créer un utilisateur

POST /api/accounts/login/ : login, reçoit access + refresh

POST /api/accounts/refresh/ : régénérer un access token

POST /api/accounts/logout/ : blacklister un refresh token

GET /api/accounts/me/ : profil utilisateur connecté

Tokens personnalisés avec email, prénom, etc.

⚙️ Tâches Celery
Démarrer un worker :

celery -A config worker --loglevel=info

Démarrer le scheduler (beat) :

celery -A config beat --loglevel=info

Voir/planifier des tâches dans /admin (grâce à django-celery-beat)

📡 WebSocket en temps réel
URL : ws://localhost:8000/ws/logs/

Affiche chaque nouvelle ligne ajoutée à logs/app.log

Utilise Redis comme backend channels_redis et daphne comme serveur ASGI

🪵 API de logs
Méthode	Endpoint	Action
GET	/api/logs/	Voir les logs récents (paginés)
GET	/api/logs/?level=ERROR&page=2	Filtrer par niveau de log
POST /api/logs/clear/	Vider le fichier logs/app.log

🛡️ Sécurité & Bonnes pratiques
.env non versionné (SECRET_KEY, DB, etc.)

venv/, __pycache__/, logs/ ignorés via .gitignore

IsAdminUser sur les vues sensibles (logs/, clear/, etc.)

JWT avec rotation sécurisée des tokens + blacklist

🧪 Tests de base

python manage.py test
À compléter selon vos apps

📋 Prérequis
Python ≥ contenu de python_version.txt

PostgreSQL (par défaut sur le port 11002)

Redis (par défaut sur le port 6379)

Daphne ou python manage.py runserver en dev

👤 Auteur
Développé par Bachir MOSTAFA
Licence : MIT

