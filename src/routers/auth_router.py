from typing import List
from fastapi import APIRouter, status, HTTPException, Depends
from prisma import Prisma
from src.models.register_model import RegisterUserResponse, RegisterUserRequest
from src.models.login_model import LoginUserRequest
import httpx
import os
import bcrypt

authRoute = APIRouter()

# Configuración de Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

# Dependencia para manejar la conexión a la base de datos
async def get_db():
    db = Prisma()
    await db.connect()
    try:
        yield db
    finally:
        await db.disconnect()

@authRoute.post("/register", response_model=RegisterUserResponse)
async def register_user(
    data: RegisterUserRequest,
    db: Prisma = Depends(get_db)
):
    # 1. Crear usuario en Supabase Auth
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{SUPABASE_URL}/auth/v1/admin/users",
            headers={
                "apikey": SUPABASE_API_KEY,
                "Authorization": f"Bearer {SUPABASE_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "email": data.email,
                "password": data.password,
                "user_metadata": {  # Añadir metadatos si es necesario
                    "nombre": data.nombre,
                    "apellido": data.apellido,
                    "username": data.username
                }
            }
        )

    if res.status_code not in (200, 201):
        error_detail = res.json().get("message", "Error desconocido de Supabase")
        raise HTTPException(
            status_code=400,
            detail=f"Error al crear usuario en Supabase: {error_detail}"
        )

    user_info = res.json()
    user_id = user_info.get("id")
    if not user_id:
        raise HTTPException(
            status_code=500,
            detail="No se pudo obtener el ID del usuario de Supabase"
        )

    # 2. Crear perfil en Prisma
    try:
        profile = await db.profile.create(
            data={
                "user_id": user_id,
                "nombre": data.nombre,
                "apellido": data.apellido,
                "username": data.username,
                "email": data.email
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear perfil en la base de datos: {str(e)}"
        )

    return RegisterUserResponse(
        message="Usuario registrado con éxito",
        user_id=user_id,
        profile=profile
    )
#LA PARTE QUE NOS INTERESA EN ESTE MOMENTO ES LA DE LOGIN
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Ejemplo con bcrypt; asegúrate de que esté instalado e importado correctamente.
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

@authRoute.post("/login")
async def login_user(
    data: LoginUserRequest,   # Usamos el modelo exclusivo para login
    db: Prisma = Depends(get_db)
):
    try:
        # Buscar el perfil por username e incluir el usuario relacionado para acceder a la contraseña encriptada.
        profile = await db.profile.find_first(
            where={
                "username": data.username
            },
            include={
                "user": True  # Esto se encarga de traer los datos del usuario relacionado (incluyendo encrypted_password)
            }
        )
        
        if not profile:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )
        
        # Verificar la contraseña
        user = profile.user
        if not user or not user.encrypted_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )
        
        if not verify_password(data.password, user.encrypted_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )
        
        # Si todo es correcto, se puede devolver un token o los datos del usuario.
        return {
            "message": "Inicio de sesión exitoso",
            "user": {
                "id": user.id,
                "username": profile.username,
                "email": profile.email  # O cualquier otro dato que quieras enviar
            }
        }
    except HTTPException as http_err:
        # Re-lanzar los HTTPException ya definidos
        raise http_err
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )