from prisma import Prisma
from fastapi import APIRouter,HTTPException
from config import supabase
from src.models.user_model import User

authRouter = APIRouter(tags=["Auth"])

@authRouter.post("/register")
async def register(user: User):
    response = supabase.auth.sign_up({"email": user.email, "password": user.password})
    
    if "error" in response:
        raise HTTPException(status_code=400, detail="Error al registrar usuario")
    
    return {"message": "Usuario registrado con éxito", "data": response}

# Login de usuario
@authRouter.post("/login")
async def login(user: User):
    response = supabase.auth.sign_in_with_password({"email": user.email, "password": user.password})
    print(user)
    if "error" in response:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"message": "Login exitoso", "session": response.session}

# Verificar sesión del usuario
@authRouter.get("/me")
async def get_me(token: str):
    user = supabase.auth.get_user(token)

    if not user or "error" in user:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    return {"user": user}