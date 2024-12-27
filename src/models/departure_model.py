from datetime import datetime
from pydantic import BaseModel


# Se crea un modelo Pydantic para representar una tarea individual
class Departure(BaseModel):
    id: int | None = None

    destiny: str

    create_at: datetime

class Departure_product(BaseModel):
    order: int | None = None

    id_departure: int | None = None

    id_product: int | None = None

    quantity: int

    unit_price: float
