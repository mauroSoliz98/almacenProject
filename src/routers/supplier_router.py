from fastapi import APIRouter, HTTPException
from prisma import Prisma
from src.models.supplier_model import Supplier

db = Prisma()
supplierRouter = APIRouter()

#Muestra la lista de todo los elemntos
@supplierRouter.get("/")
async def get_items():
    await db.connect()
    data = await db.supplier.find_many()
    await db.disconnect()
    return data
    

#Se encarga de mostrar un elemento en concreto
@supplierRouter.get("/{supplier_id}")
async def get_item(supplier_id:int):
  await db.connect()
  try:
    supplier = await db.supplier.find_many(where={'id':supplier_id})
    if supplier:
      return supplier
    raise HTTPException(status_code=404, detail='item not found :c')
  finally:
    await db.disconnect()
  

#Añade un nuevo elemnento
@supplierRouter.post("/")
async def create_item(supplier:Supplier):
  await db.connect()
  #Agregamos el nuevo item al stock
  data = await db.supplier.create(data=supplier.model_dump())
  await db.disconnect()
  return data

#Eleminar un elemento
@supplierRouter.delete("/{supplier_id}")
async def delete_item(supplier_id: int):
    await db.connect()
    #del stock[item_id]
    data = await db.supplier.delete(where={"id": supplier_id})
    await db.disconnect()
    return data

#Actualizar un elemento
@supplierRouter.put("/{supplier_id}")
async def update_item(supplier_id: int, updatedSupplier: Supplier):
  await db.connect()
  data = await db.supplier.update(where={'id': supplier_id}, data = updatedSupplier.model_dump())
  await db.disconnect()
  return data