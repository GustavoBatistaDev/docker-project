from ninja import Router
from django.http import JsonResponse


list_fruits = Router()

@list_fruits.get('/')
def list_foods(request):
  
    return JsonResponse({'foods': ['rota2', 'usuario2']}) 