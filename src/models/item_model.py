from pydantic import BaseModel

class Item(BaseModel):
  name: str
  brand: str 
  description: str
  units: str
  unit_price: float