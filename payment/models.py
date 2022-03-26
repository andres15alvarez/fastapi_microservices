from pydantic import BaseModel
from fastapi import status
from fastapi.exceptions import HTTPException
from redis_om import HashModel
from redis_om.model.model import NotFoundError
from database import redis


class Order(HashModel):
    product_id: str
    price: int
    fee: float
    total: int
    quantity: int
    status: str # PENDING, COMPLETED, REFUNDED

    class Meta:
        database = redis

    def format(pk: str):
        order: Order = Order.get(pk)
        return {
            'product_id': order.product_id,
            'price': order.price,
            'fee': order.fee,
            'total': order.price,
            'quantity': order.quantity,
            'status': order.status
        }

    def get_or_404(pk: str):
        try:
            return Order.get(pk)
        except NotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')


class OrderCreate(BaseModel):
    product_id: str
    quantity: int
