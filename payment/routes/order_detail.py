from fastapi import APIRouter

from models import Order


order_detail_router = APIRouter()


@order_detail_router.get("/order/{pk}")
async def get_order(pk: str):
    return Order.get(pk)
