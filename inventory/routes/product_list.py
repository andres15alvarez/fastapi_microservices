from fastapi import status, APIRouter
from models import Product


product_list_router = APIRouter()


@product_list_router.get("/product")
async def get_products():
    return [Product.format(pk) for pk in Product.all_pks()]


@product_list_router.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    return product.save()
