import logging
from celery import shared_task
import datetime

logger = logging.getLogger(__name__)


@shared_task
def ping():
    now = datetime.datetime.now()
    logger.info("✅ Tâche ping exécutée depuis Celery a {now}")
    return "pong {now}"