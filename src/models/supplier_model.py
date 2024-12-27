from pydantic import BaseModel

class Supplier(BaseModel):
    supplier_name: str
    phone_number: int 
    mail: str
    location: str

class Supplier_reference(BaseModel):
    id: int


