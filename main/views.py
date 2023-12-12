from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
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
    # permission_classes = [permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CategoryList(generics.ListCreateAPIView):
    queryset = models.CourseCategory.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    email = request.POST['email']
    password = request.POST['password']
    teacher = models.Teacher.objects.filter(email=email, password=password).first()
    if teacher:
        return JsonResponse({'loggedIn': True})
    
    return JsonResponse({'loggedIn': False})

