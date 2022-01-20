from rest_framework import serializers
from .models import School, Student

class SchoolSerializer(serializers.ModelSerializer):
    
    """This class serializes the School Model"""
    class Meta:

        model = School
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    
    """This class serializes the Student Model"""
    class Meta:

        """"""
        model = Student
        fields = "__all__"
