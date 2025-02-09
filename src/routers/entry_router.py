from fastapi import APIRouter, status
from prisma import Prisma
from src.models.entry_model import Entry, Entry_product
from src.models.supplier_model import Supplier_reference
from src.models.product_model import Product_Reference
db = Prisma()
entryRoute = APIRouter()

@entryRoute.get("/")
async def get_todos():
    await db.connect()
    try:
      data = await db.entry.find_many(
        include={"supplier": True, "entry_product": {"include": {"products": True}}}
      )
      filter_data = [
        {
          "id": item.id,
          "supplier": {item.supplier.supplier_name},
          "entry_product": [
            {
              "product":product.products.name,
              "quantity": product.quantity,
              "unit_price": product.unit_price,
            } for product in item.entry_product
          ],
        "create_at": item.create_at, 
        } for item in data
      ]
    finally:
      await db.disconnect()

    return filter_data

@entryRoute.get("/{id}")
async def get_todo(id: int):
    await db.connect()
    data = await db.entry.find_unique(where={'id':id} )
    await db.disconnect()

    return data

@entryRoute.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(entry: Entry, supplier: Supplier_reference, product: Product_Reference, entry_product: Entry_product):

  await db.connect()

  new_entry = await db.entry.create(
    data= 
      {
        "id_supplier": supplier.id,
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
