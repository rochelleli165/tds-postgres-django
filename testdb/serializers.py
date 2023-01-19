from rest_framework import serializers
from testdb.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'age')