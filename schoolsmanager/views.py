from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student
from uuid import uuid4

forbidden_symbols = "!~`@#$%^&*)(_+=}{\|[]\"':;?/<>"

def index(request):

    """This endpoints tests if dev/prod is running"""
    return HttpResponse('Alive and Running')
class SchoolViewSet(viewsets.ModelViewSet):

    """This class provides all REST methods for schools endpoint"""
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):

    """This class provides all REST methods for students endpoint"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            school = serializer.validated_data.get("school")
            student_count = Student.objects.filter(school=school.id).count()
            max_student = School.objects.get(pk=school.id).maxstudents
            
            #2nd Level input strings validation, input strings must not contain forbidden characters
            for val in serializer.validated_data.values():
                if isinstance(val, str):
                    if any([item in forbidden_symbols for item in val]):
                        return Response(f"{val} contains forbidden character(s)", status=status.HTTP_400_BAD_REQUEST)
            
            #First Name and Last Name should not start with a number
            if serializer.validated_data.get("firstname")[0].isdigit() or serializer.validated_data.get("lastname")[0].isdigit():
                return Response(f"Name cannot begin with digit(s)", status=status.HTTP_400_BAD_REQUEST)

            #Maintain the maximum number of students a school can take
            if (student_count + 1) > max_student:
                return Response("maximum number of student reached", status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(str(uuid4()).replace("-", ""), status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolStudentViewSet(viewsets.ModelViewSet):

    """This class provides all REST methods for schools/student endpoint"""
    serializer_class = StudentSerializer

    def get_queryset(self):

        return Student.objects.filter(school=self.kwargs['school_pk'])



