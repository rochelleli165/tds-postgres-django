from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from testdb.models import Teacher
from testdb.serializers import TeacherSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            teachers = teachers.filter(title__icontains=title)
        
        teachers_serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        teacher = Teacher.objects.get(pk=pk) 
    except Teacher.DoesNotExist: 
        return JsonResponse({'message': 'The teacher does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        teacher_serializer = TeacherSerializer(teacher) 
        return JsonResponse(teacher_serializer.data) 
    elif request.method == 'PUT': 
        teacher_data = JSONParser().parse(request) 
        teacher_serializer = TeacherSerializer(teacher, data=teacher_data) 
        if teacher_serializer.is_valid(): 
            teacher_serializer.save() 
            return JsonResponse(teacher_serializer.data) 
        return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        teacher.delete() 
        return JsonResponse({'message': 'Teacher was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)    
    elif request.method == 'DELETE':
        count = Teacher.objects.all().delete()
        return JsonResponse({'message': '{} Teachers were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def teacher_list_published(request):
    # GET all published teachers
    teacher = Teacher.objects.filter(published=True)
        
    if request.method == 'GET': 
        teacher_serializer = TeacherSerializer(teacher, many=True)
        return JsonResponse(teacher_serializer.data, safe=False)