from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.routers.product_router import itemRouter
from src.routers.departure_router import departureRoute
from src.routers.entry_router import entryRoute
from src.routers.supplier_router import supplierRouter

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura Jinja2Templates para apuntar al directorio dist
templates = Jinja2Templates(directory="../dist")

# Monta el directorio dist para servir archivos estáticos
app.mount('/assets', StaticFiles(directory="dist/assets"), name='assets')

@app.get("/")
def read_root():
    with open("dist/index.html", "r") as file:
        return HTMLResponse(content=file.read(), media_type="text/html")


# Incluye los routers
app.include_router(prefix="/api/products", router=itemRouter)
app.include_router(prefix="/api/departure", router=departureRoute)
app.include_router(prefix="/api/entry", router=entryRoute)
app.include_router(prefix="/api/suppliers", router=supplierRouter)

'''
NOTA: 
PONER ESTE COMANDO EN START COMMAND DE RENDER
uvicorn src.main:app --host 0.0.0.0 --port $PORT
'''