from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializer import BirinchiSerializer,IkkinchiSerializer,UchinchiSerializer,TortinchiSerializer
from .models import Salom1,Salom2,Salom3,Salom4
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BirinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = BirinchiSerializer
    queryset = Salom1.objects.all()
    
class IkkinchiListCreateAPiView(ListCreateAPIView):
    serializer_class = IkkinchiSerializer
    queryset = Salom2.objects.all()
    
class UchinchiViewSet(ModelViewSet):
    queryset = Salom3.objects.all()
    serializer_class = UchinchiSerializer
    permission_classes = [IsAuthenticated]
    
class TortinchiViewSet(ModelViewSet):
    queryset = Salom4.objects.all()
    serializer_class = TortinchiSerializer
    permission_classes = [IsAuthenticated]
