from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from documents.models import Document
from .models import Ingestion
from .serializers import IngestionSerializer
from .tasks import process_ingestion

class IngestionTriggerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, document_id):
        try:
            document = Document.objects.get(id=document_id)
            ingestion = Ingestion.objects.create(document=document)
            process_ingestion.delay(ingestion.id) #This is just to simulate async processing
            return Response({'message': 'Ingestion triggered', 'ingestion_id': ingestion.id})
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)

class IngestionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ingestions = Ingestion.objects.all().order_by('-started_at')
        serializer = IngestionSerializer(ingestions, many=True)
        return Response(serializer.data)
