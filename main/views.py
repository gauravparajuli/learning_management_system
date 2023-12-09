from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from . import serializers
from . import models

# Create your views here.
# class TeacherList(APIView):
#     def get(self, request):
#         teachers = models.Teacher.objects.all()
#         serializer = serializers.TeacherSerializer(teachers, many=True)
#         return Response(serializer)

class TeacherList(generics.ListCreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
