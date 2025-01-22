from typing import List
from fastapi import APIRouter, status, HTTPException
from prisma import Prisma
from src.models.departure_model import Departure, DepartureItem


db = Prisma()
departureRoute = APIRouter()


@departureRoute.get("/")
async def get_todos():
    await db.connect()
    try:
        # Recupera datos de departure_product incluyendo relaciones
        data = await db.departure_product.find_many(
            include={"departures": True, "products": True}
        )

        # Filtra los datos para excluir los IDs
        filtered_data = [
            {
                "departure": (
                    {
                        "id": item.departures.id,
                        "create_at": item.departures.create_at,
                        "destiny": item.departures.destiny,
                    }
                    if item.departures
                    else None
                ),
                "product": (
                    {
                        "name": item.products.name,
                    }
                    if item.products
                    else None
                ),
                "order": item.order,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
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
    data = await db.departure.find_unique(where={"id": id})
    await db.disconnect()
    return data


@departureRoute.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(items: List[DepartureItem]):

    await db.connect()

    # Verificar que todos los productos existen
    product_ids = [item.product.id for item in items]
    existing_products = await db.product.find_many(where={"id": {"in": product_ids}})
    existing_product_ids = {product.id for product in existing_products}

    for item in items:
        if item.product.id not in existing_product_ids:
            await db.disconnect()
            raise HTTPException(status_code=400, detail=f"Product with id {item.product.id} does not exist")

    # Agregamos los nuevos items al stock
    new_departure = await db.departure.create(
        data={
            "destiny": items[0].departure.destiny,
            "create_at": items[0].departure.create_at,
            "departure_product": {
                "create": [
                    {
                        "id_product": item.product.id,
                        "quantity": item.departure_product.quantity,
                        "unit_price": item.departure_product.unit_price,
                    }
                    for item in items
                ]
            },
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

    data = await db.departure.update(where={"id": id}, data=departure.model_dump())
    await db.disconnect()
    return data