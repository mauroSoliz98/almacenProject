from fastapi import APIRouter, status
from prisma import Prisma
from src.models.entry_model import Entry, Entry_product
from src.models.supplier_model import SupplierReference
from src.models.product_model import ProductReference
db = Prisma()
entryRoute = APIRouter()

@entryRoute.get("/")
async def get_todos():
    await db.connect()
    data = await db.entry.find_many()
    await db.disconnect()

    return data

@entryRoute.get("/{id}")
async def get_todo(id: int):
    await db.connect()
    data = await db.entry.find_many(where={'id':id} )
    await db.disconnect()

    return data

@entryRoute.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(entry: Entry, supplier: SupplierReference, product: ProductReference, entry_product: Entry_product):

  await db.connect()

  new_entry = await db.entry.create(
    data= 
      {
        "id_supplier": supplier.id_supplier,
        "create_at": entry.create_at,
        "entry_product": {
            "create": [
                {
                    "id_product": product.id,
                    "quantity": entry_product.quantity,
                    "unit_price": entry_product.unit_price,
                }
            ]
        }
      },   
    )

  await db.disconnect()
  return new_entry


@entryRoute.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int):

    await db.connect()
    data = await db.entry.delete(where={"id": id})
    await db.disconnect()
    return data

@entryRoute.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_entry(id: int, entry: Entry):
  await db.connect()

  data = await db.entry.update(where={'id': id}, data=entry.model_dump())
  await db.disconnect()
  return data