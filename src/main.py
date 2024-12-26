from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from src.routers.item_router import itemRouter


app = FastAPI()


origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#MUCHO OJO: AL PARECER EL ENPOINT UTILIZA LOS ATRIBUTO DEL BASE MODEL Y NO LOS DE 
#LA BD POR LO QUE LOS ATRIBUTOS DEL BASE MODEL TIENES QUE SER IGUALES A LOS DE LA
#BD

#Ruta raiz
@app.get("/")
def read_root():
    return {"Hello": "World"}
app.include_router(prefix='/api/items', router=itemRouter)