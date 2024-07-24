from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Haciendolo con una funcion:

# @api_view(['GET']) el decorador @api_view es necesario para especificar qué métodos HTTP (GET, POST, etc.) deben ser manejados por esa vista.
# def task_list(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return JsonResponse(serializer.data, safe=False)
