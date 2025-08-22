from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Case Técnico - API de Métricas")

from login_routes import login_router
from metrics_routes import metrics_router

app.include_router(login_router)
app.include_router(metrics_router)


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



