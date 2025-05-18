from celery import shared_task
from .models import Ingestion
from django.utils.timezone import now
import time

@shared_task
def process_ingestion(ingestion_id):
    try:
        ingestion = Ingestion.objects.get(id=ingestion_id)
        ingestion.status = "IN_PROGRESS"
        ingestion.save()

        time.sleep(10)

        ingestion.status = "COMPLETED"
        ingestion.completed_at = now()
        ingestion.save()
    except Exception as e:
        ingestion.status = "FAILED"
        ingestion.error_message = str(e)
        ingestion.save()
