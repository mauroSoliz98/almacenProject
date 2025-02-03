import os
from fastapi import FastAPI, HTTPException, status
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
async def serve_react():
    return HTMLResponse(open("dist/index.html").read())

@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    """Sirve index.html para cualquier ruta desconocida, permitiendo que React maneje el enrutamiento."""
    if not full_path.startswith("api"):  # No sobrescribir las rutas de la API
        index_path = "dist/index.html"
        if os.path.exists(index_path):
            return HTMLResponse(open(index_path).read())
    raise HTTPException(status_code=404, detail="Not Found")


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