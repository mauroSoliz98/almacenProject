from prisma import Prisma
from fastapi import APIRouter,HTTPException, Header, Request
from config import supabase
from src.models.user_model import User
# from src.middleware.auth_middleware import BLACKLISTED_TOKENS

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
    try:
        response = supabase.auth.sign_in_with_password({"email": user.email, "password": user.password})
        return {"message": "Login exitoso", "session": response.session}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

# Verificar sesión del usuario
@authRouter.get("/me")
async def get_me(token: str):
    user = supabase.auth.get_user(token)

    if not user or "error" in user:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    return {"user": user}

@authRouter.post("/logout")
async def logout(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token de autorización requerido")
    # Revocar la sesión en Supabase (esto invalida el refresh_token asociado)
    response = supabase.auth.sign_out()
    if response and "error" in response:
        raise HTTPException(status_code=400, detail="Error al cerrar sesión")
    return {"message": "Sesión cerrada con éxito"}
