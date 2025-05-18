echo "Starting Celery worker..."
celery -A django_project worker --loglevel=info
