from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.routers.product_router import itemRouter
from src.routers.departure_router import departureRoute
from src.routers.entry_router import entryRoute
from src.routers.supplier_router import supplierRouter
from src.routers.auth_router import authRoute

app = FastAPI(docs_url=None, redoc_url=None)

origins = ["http://localhost:5173", "https://almacenproject-zu5h.onrender.com"]

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


# Incluye los routers
app.include_router(itemRouter, prefix="/api/products")
app.include_router(departureRoute, prefix="/api/departure")
app.include_router(entryRoute, prefix="/api/entry")
app.include_router(supplierRouter, prefix="/api/suppliers")
app.include_router(authRoute, prefix="/api/auth")


@app.get("/")
async def serve_react():
    return HTMLResponse(open("dist/index.html").read())

@app.exception_handler(404)
async def exception_404_handler(request, exc):
    return FileResponse("dist/index.html")
'''
NOTA: PONER EL SIGUEINTE COMANDO EN RENDER
prisma && uvicorn main:app --host 0.0.0.0 --port $PORT
'''