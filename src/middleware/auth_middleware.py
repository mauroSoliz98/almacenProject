from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from supabase import create_client
import os

# Cargar credenciales de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Rutas públicas (permitidas sin autenticación)
PUBLIC_ROUTES = [
    "/auth/login",
    "/auth/register",
]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Permitir acceso a rutas públicas sin autenticación
        print(request.url.path)
        if request.url.path in PUBLIC_ROUTES:
            return await call_next(request)
        
        # Extraer el token del encabezado Authorization
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Token de autorización requerido")
        
        # Validar el token con Supabase
        token = token.split("Bearer ")[1]
        response = supabase.auth.get_user(token)

        if "error" in response:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # Adjuntar usuario autenticado a la solicitud
        request.state.user = response.user
        return await call_next(request)
