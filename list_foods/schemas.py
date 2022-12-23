from typing import List, Dict, Union
from ninja import  ModelSchema
from .models import Product as Model_Product


class Product(ModelSchema):
    class Config:
        model = Model_Product
        model_fields = "__all__"
    