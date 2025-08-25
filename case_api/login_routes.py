from fastapi import APIRouter, HTTPException
from schemas import LoginData
from sqlalchemy import text
from database.db import get_engine

login_router = APIRouter(prefix="/login", tags=["login"])

@login_router.post("/")
def login(data: LoginData):
    """
    Faz login consultando o banco (tabela 'usuarios').
    Retorna a role do usuário (admin/user) se as credenciais forem válidas.
    """
    engine = get_engine()
    with engine.connect() as conn:
        row = conn.execute(
            text("""
                SELECT role
                FROM usuarios
                WHERE email = :email AND password = :password
                LIMIT 1
            """),
            {"email": data.email, "password": data.password}
        ).fetchone()

    if not row:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    role = row[0]
    return {"message": "Login realizado com sucesso!", "role": role}