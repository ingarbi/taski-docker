from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
