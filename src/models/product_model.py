from pydantic import BaseModel

class Product(BaseModel):
  id: int | None = None
  name: str 
  brand: str 
  description: str
  unit_price: float
  units: str

class Product_Reference(BaseModel):
  
  id: int