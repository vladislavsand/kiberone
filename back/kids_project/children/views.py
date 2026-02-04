from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Child
from .serializers import ChildSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

@api_view(['GET'])
def client_list(request):
    clients = Child.objects.filter(status='client')
    serializer = ChildSerializer(clients, many=True)
    return Response(serializer.data)

