from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
product_db = [] #temporary in-memory storage

class ProductCreate(BaseModel):
    name : str
    price: float
    stock: int
    comment:list[str] = []

@app.post("/product")
def create_product(product: ProductCreate):
    new_product = product.model_dump()
    new_product["id"] = len(product_db)+1
    product_db.append(new_product)
    return new_product

@app.get("/products")
def list_products():
    return product_db

@app.get("/products/{product_id}")
def get_product(product_id:int):
    for item in product_db:
        if item["id"] == product_id:
            return item
        