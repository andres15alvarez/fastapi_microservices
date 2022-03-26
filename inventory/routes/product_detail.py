from fastapi import APIRouter
from fastapi.responses import Response
from models import Product, ProductUpdate


product_detail_router = APIRouter()


@product_detail_router.get("/product/{pk}")
async def get_product(pk: str):
    return Product.get_or_404(pk)

@product_detail_router.put("/product/{pk}")
async def update_product(pk: str, product: ProductUpdate):
    product_to_update = Product.get_or_404(pk)
    product_to_update.update(**product.dict())
    return product_to_update.dict()

@product_detail_router.delete("/product/{pk}")
async def delete_product(pk: str):
    product = Product.get_or_404(pk)
    product.active = 'False'
    product.save()
    return product