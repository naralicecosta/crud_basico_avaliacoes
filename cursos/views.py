from django.shortcuts import render

# Create your views here.
from rest.framework.views import APIView
from rest.framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(cursos, many = True)
        serializer.is_valid(raise_exceptions = True)
        serializer.save()
        return Response(serializer.data, tatus=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many = True)
        return Response(serializer.data)