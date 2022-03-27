from celery.result import AsyncResult
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from api.tasks import create_task
from api.serializers import AdvertSerializer
from api.models import Advert


class AdvertsViewSet(ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


@api_view(['POST'])
def run_task(request):
    task = create_task.delay(request.data)
    result = {
        'task_id': task.id
    }
    return JsonResponse(result, status=202)


@api_view(['GET'])
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
    }
    return JsonResponse(result, status=202)
