from pydantic import BaseModel

class Product(BaseModel):
  name: str 
  brand: str 
  description: str
  units: str
  unit_price: float

class Product_Reference(BaseModel):
  id: int