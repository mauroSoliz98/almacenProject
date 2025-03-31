from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from gotrue.errors import AuthApiError
from fastapi.responses import JSONResponse
from config import supabase

class AuthMiddleware(BaseHTTPMiddleware):
    
    # Rutas públicas (permitidas sin autenticación)
    _PUBLIC_ROUTES = {"/auth/login", "/auth/register"}
    async def dispatch(self, request: Request, call_next):

        if request.url.path in self._PUBLIC_ROUTES:
            return await call_next(request)
        
        # Extraer el token del encabezado Authorization
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Token de autorización requerido"})
        
        token = token.split("Bearer ")[1]

        try:
            response = supabase.auth.get_user(token)

            # Adjuntar usuario autenticado a la solicitud
            request.state.user = response.user
            return await call_next(request)

        except AuthApiError as e:
            # Captura errores de autenticación y devuelve 401 en lugar de 500
             return JSONResponse(status_code=401, content={"detail": "Token inválido o expirado"})
