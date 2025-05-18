from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doc_mgmt import settings
from ingestions.views import IngestionTriggerView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/documents/', include('documents.urls')),
    path('api/ingestions/', include('ingestions.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)