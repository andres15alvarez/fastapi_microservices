from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product_list import product_list_router
from routes.product_detail import product_detail_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(product_list_router)
app.include_router(product_detail_router)

@app.get("/")
async def root():
    return {"message": "hello world"}
