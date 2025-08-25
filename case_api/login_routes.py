from fastapi import APIRouter
from schemas import LoginData
from data import users_df

login_router = APIRouter(prefix="/login", tags=["login"])

# --- Função que valida usuário ---
def authenticate_user(login_data: LoginData):
    email = login_data.email
    password = login_data.password  

    user = users_df[(users_df["email"] == email) & (users_df["password"] == password)]
    if not user.empty:
        return user.iloc[0]["role"]
    return None

# --- Endpoint de Login ---
@login_router.post("/")
def login(data: LoginData):
    role = authenticate_user(data)
    if not role:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "Login realizado com sucesso!", "role": role}