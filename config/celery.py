import os
from celery import Celery

# 1. Configure Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.conf import settings  # ⚠️ après os.environ

import logging.config
logging.config.dictConfig(settings.LOGGING)

# 2. Crée l'app Celery
app = Celery("config")

# 3. Charge les settings
app.config_from_object("django.conf:settings", namespace="CELERY")

# 4. Auto-découverte des tâches
app.autodiscover_tasks()