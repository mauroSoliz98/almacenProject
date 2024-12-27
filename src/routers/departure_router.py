from fastapi import APIRouter, status
from prisma import Prisma
from src.models.departure_model import Departure, Departure_product
from src.models.product_model import ProductReference
db = Prisma()
departureRoute = APIRouter()

@departureRoute.get("/")
async def get_todos():
    await db.connect()
    data = await db.departure.find_many()
    await db.disconnect()
    #data = supabase.table("Departure").select('*').execute()
    return data

@departureRoute.get("/{id}")
async def get_todo(id: int):
    await db.connect()
    data = await db.departure.find_many(where={'id':id} )
    await db.disconnect()
    #data = supabase.table("Departure").select("*").eq("id", id).execute()
    return data

@departureRoute.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(departure: Departure, product: ProductReference, departure_product: Departure_product):

  await db.connect()
  #Agregamos el nuevo item al stock
  new_departure = await db.departure.create(
    data = 
      {
        "destiny": departure.destiny,
        "create_at": departure.create_at,
        "departure_product": {
            "create": [
                {
                    "id_product": product.id,
                    "quantity": departure_product.quantity,
                    "unit_price": departure_product.unit_price,
                }
            ]
        }
      },   
    )

  await db.disconnect()
  return new_departure
    #data = supabase.table('Departure').insert(todo.dict(Departure)).execute()

@departureRoute.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int):
    #data = supabase.table('Departure').delete().eq('id', id).execute()
    await db.connect()
    #del stock[item_id]
    data = await db.departure.delete(where={"id": id})
    await db.disconnect()
    return data

@departureRoute.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_departure(id: int, departure: Departure):
  await db.connect()

  data = await db.departure.update(where={'id': id}, data=departure.model_dump())
  await db.disconnect()
  return data
