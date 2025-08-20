from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
import pandas as pd

# --- Carregando os dados dos CSVs ---
users_df = pd.read_csv("users.csv")     
metrics_df = pd.read_csv("metrics.csv")  

# Criando a aplicação FastAPI
app = FastAPI(title="Case Técnico - API de Métricas")

# --- Função auxiliar para autenticar usuário ---
def authenticate_user(username: str, password: str):
    """
    Verifica se o usuário existe no CSV e se a senha confere.
    Retorna o papel do usuário se válido, senão None.
    """
    user = users_df[(users_df["username"] == username) & (users_df["password"] == password)]
    if not user.empty:
        return user.iloc[0]["role"]  # retorna 'admin' ou outro papel
    return None


# --- Endpoint de Login ---
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Faz login do usuário.
    Usa email como 'username' e senha como 'password'.
    """
    role = authenticate_user(form_data.username, form_data.password)
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
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    # --- Ordenação por coluna ---
    if order_by and order_by in df.columns:
        df = df.sort_values(by=order_by)

    # --- Controle de permissão ---
    if role != "admin":  
        if "cost_micros" in df.columns:
            df = df.drop(columns=["cost_micros"])

    return df.to_dict(orient="records")  # converte para lista de dicionários JSON
