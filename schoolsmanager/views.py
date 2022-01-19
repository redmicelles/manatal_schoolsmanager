from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student
from uuid import uuid4

def index(request):
    return HttpResponse('Alive and Running')
class SchoolViewSet(viewsets.ModelViewSet):

    """"""
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def create(self, request):
        print(request.data)
        return Response(uuid4(), status=201)

class StudentViewSet(viewsets.ModelViewSet):

    """"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(str(uuid4()).replace("-", ""), status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



