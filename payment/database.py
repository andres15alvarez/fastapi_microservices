import os
from redis_om import get_redis_connection
from dotenv import load_dotenv


load_dotenv()
redis = get_redis_connection(
    host=os.environ.get('REDIS_HOST'),
    port=os.environ.get('REDIS_PORT'),
    password=os.environ.get('REDIS_PASSWORD'),
    decode_responses=True
)