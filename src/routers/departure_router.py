from fastapi import APIRouter, status, HTTPException
from prisma import Prisma
from src.models.departure_model import Departure, Departure_product
from src.models.product_model import Product_Reference
db = Prisma()
departureRoute = APIRouter()

@departureRoute.get("/")
async def get_todos():
    await db.connect()
    try:
        # Recupera datos de departure_product incluyendo relaciones
        data = await db.departure_product.find_many(include={
            'departures': True,
            'products': True
        })

        # Filtra los datos para excluir los IDs
        filtered_data = [
            {               
                'departure': {
                    'id': item.departures.id,
                    'create_at': item.departures.create_at,
                    'destiny': item.departures.destiny
                } if item.departures else None,
                'product': {
                    'name': item.products.name,
                } if item.products else None,
                'order':item.order,
                'quantity': item.quantity,
                'unit_price': item.unit_price
            }
            for item in data
        ]
        print(filtered_data)
        return filtered_data
    finally:
        await db.disconnect()



@departureRoute.get("/{id}")
async def get_todo(id: int):
    await db.connect()
    data = await db.departure.find_unique(where={'id':id} )
    await db.disconnect()
    return data



@departureRoute.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(departure: Departure, product: Product_Reference, departure_product: Departure_product):

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

@departureRoute.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_todo(id: int):
    await db.connect()
    data = await db.departure.delete(where={"id": id})
    await db.disconnect()
    return data

@departureRoute.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_departure(id: int, departure: Departure):
  await db.connect()

  data = await db.departure.update(where={'id': id}, data=departure.model_dump())
  await db.disconnect()
  return data
