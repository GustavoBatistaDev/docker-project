from ninja import NinjaAPI
from django.http import JsonResponse
from list_foods.api import list_foods_router
from pacientes.api import list_fruits

api = NinjaAPI()

api.add_router('list_foods/', list_foods_router )

api.add_router('list_fruits/', list_fruits )

