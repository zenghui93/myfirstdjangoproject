from rest_framework.viewsets import ModelViewSet

from .serializers import ListSerializer, RecordSerializer, CategorySerializer
from .models import List, Record, Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer



class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


