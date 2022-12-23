from ninja import NinjaAPI
from django.http import JsonResponse
from..tasks import my_task


api = NinjaAPI()

@api.get('/')
def list_foods(request):
    my_task.delay()
    return JsonResponse({'foods': ['banana', 'ricardao']}) 