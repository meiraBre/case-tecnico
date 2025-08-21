from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# --- Modelo para o corpo do login ---
class LoginData(BaseModel):
    email: str
    password: str

app = FastAPI(title="Case Técnico - API de Métricas")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Carrega a leitura do arquivo fora da função, para melhorar a performance ---
users_df = pd.read_csv("users.csv")
metrics_df = pd.read_csv("metrics.csv")

# --- Função que valida usuário ---
def authenticate_user(login_data: LoginData):
    email = login_data.email
    password = login_data.password  

    user = users_df[(users_df["email"] == email) & (users_df["password"] == password)]
    if not user.empty:
        return user.iloc[0]["role"]
    return None

# --- Endpoint de Login ---
@app.post("/login")
def login(data: LoginData):
    role = authenticate_user(data)
    if not role:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "Login realizado com sucesso!", "role": role}

# --- Endpoint para listar métricas ---
@app.get("/metrics")
def get_metrics(role: str, order_by: str = None, start_date: str = None, end_date: str = None):
    """
    Retorna métricas em formato JSON.
    - role: 'admin' ou 'user' (controla visualização de cost_micros)
    - order_by: coluna para ordenar
    - start_date / end_date: filtrar por intervalo de datas
    """

    df = metrics_df.copy()

    # --- Filtro por data ---
    df["date"] = pd.to_datetime(df["date"])
    if start_date and end_date:
        df = df[(df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))]

    # --- Ordenação por coluna ---
    if order_by and order_by in df.columns:
        df = df.sort_values(by=order_by)

    # --- Controle de permissão ---
    if role != "admin":  
        if "cost_micros" in df.columns:
            df = df.drop(columns=["cost_micros"])

    return df.to_dict(orient="records")  # converte para lista de dicionários JSON
