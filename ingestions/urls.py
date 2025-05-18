from django.urls import path
from .views import IngestionTriggerView, IngestionListView

urlpatterns = [
    path('<int:document_id>/trigger/', IngestionTriggerView.as_view(), name='trigger-ingestion'),
    path('status/', IngestionListView.as_view(), name='ingestion-status'),
]
