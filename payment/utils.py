import time
from database import redis
from models import Order


def complete_order(order: Order):
    order.status = 'completed'
    time.sleep(5)
    order.save()
    redis.xadd('order_completed', order.dict(), '*')