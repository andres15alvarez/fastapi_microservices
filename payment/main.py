from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.order_list import order_list_router
from routes.order_detail import order_detail_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(order_list_router)
app.include_router(order_detail_router)

@app.get("/")
async def root():
    return {"message": "hello world"}
