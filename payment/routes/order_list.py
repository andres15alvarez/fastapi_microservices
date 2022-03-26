import requests
from fastapi import APIRouter, BackgroundTasks, status
from fastapi.exceptions import HTTPException
from models import Order, OrderCreate
from utils import complete_order


order_list_router = APIRouter()


@order_list_router.get("/order")
async def get_orders():
    return [Order.format(pk) for pk in Order.all_pks()]


@order_list_router.post("/order", status_code=status.HTTP_201_CREATED)
async def create_order(request: OrderCreate, background_tasks: BackgroundTasks):
    req = requests.get(f'http://localhost:8000/product/{request.product_id}')
    product = req.json()
    if req.status_code != status.HTTP_200_OK:
        raise HTTPException(req.status_code, product['detail'])
    order = Order(
        product_id=request.product_id,
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=request.quantity,
        status='pending'
    )
    order.save()
    background_tasks.add_task(complete_order, order)
    return order