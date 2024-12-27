from datetime import datetime
from pydantic import BaseModel


# Se crea un modelo Pydantic para representar una tarea individual
class Entry(BaseModel):
    id: int | None = None

    id_supplier: int | None = None

    create_at: datetime

class Entry_product(BaseModel):
    order: int | None = None

    id_entry: int | None = None

    id_product: int | None = None

    quantity: int

    unit_price: float
