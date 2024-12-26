from prisma import Prisma
from fastapi import APIRouter,HTTPException
from src.models.item_model import Item

db = Prisma()
itemRouter = APIRouter()

#Muestra la lista de todo los elemntos
@itemRouter.get("/")
async def get_items():
    await db.connect()
    product = await db.product.find_many()
    await db.disconnect()
    return product
    

#Se encarga de mostrar un elemento en concreto
@itemRouter.get("/{item_id}")
async def get_item(item_id:int):
  await db.connect()
  try:
    item = await db.product.find_many(where={'id':item_id})
    if item:
      return item
    raise HTTPException(status_code=404, detail='item not found :c')
  finally:
    await db.disconnect()
  

#Añade un nuevo elemnento
@itemRouter.post("/")
async def create_item(item:Item):
  await db.connect()
  #Agregamos el nuevo item al stock
  data = await db.product.create(data=item.model_dump())
  await db.disconnect()
  return data

#Eleminar un elemento
@itemRouter.delete("/{item_id}")
async def delete_item(item_id: int):
    await db.connect()
    #del stock[item_id]
    data = await db.product.delete(where={"id": item_id})
    await db.disconnect()
    return data

#Actualizar un elemento
@itemRouter.put("/{item_id}")
async def update_item(item_id: int, updatedItem: Item):
  await db.connect()
  data = await db.product.update(where={'id': item_id}, data = updatedItem.model_dump())
  await db.disconnect()
  return data