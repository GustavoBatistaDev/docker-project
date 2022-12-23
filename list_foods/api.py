from ninja import Router
from .tasks import my_task
from .schemas import Product as Schema_Product
list_foods_router = Router()
from .models import Product as Model_Product


@list_foods_router.post('/', response=Schema_Product)
def list_foods(request, product:Schema_Product):

    my_task.delay()

    var_product = Model_Product.objects.get(id=1)
    return var_product