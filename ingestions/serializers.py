from rest_framework import serializers
from .models import Ingestion

class IngestionSerializer(serializers.ModelSerializer):
    document_title = serializers.ReadOnlyField(source='document.title')

    class Meta:
        model = Ingestion
        fields = '__all__'
