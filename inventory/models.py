from typing import Optional
from fastapi import HTTPException, status
from pydantic import BaseModel
from redis_om import HashModel
from redis_om.model.model import NotFoundError
from database import redis


class ProductUpdate(BaseModel):
    price: int
    quantity: int


class Product(HashModel):
    name: str
    price: int
    quantity: int
    active: Optional[str] = 'True'

    class Meta:
        database = redis

    def format(pk: str):
        product = Product.get(pk)
        return {
            'id': product.pk,
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
            'active': product.active
        }

    def get_or_404(pk: str):
        try:
            return Product.get(pk)
        except NotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')