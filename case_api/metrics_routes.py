from fastapi import APIRouter
from data import metrics_df
import pandas as pd

metrics_router = APIRouter(prefix="/metrics", tags=["metrics"])

# --- Endpoint para listar métricas ---
@metrics_router.get("/")
def get_metrics(
    role: str,
    order_by: str = None,
    start_date: str = None,
    end_date: str = None,
    limit: int = None,
    desc: bool = False
):
    """
    Retorna métricas em formato JSON.
    - role: 'admin' ou 'user' (controla visualização de cost_micros)
    - order_by: coluna para ordenar
    - start_date / end_date: filtrar por intervalo de datas
    - limit: quantidade máxima de registros
    - desc: se True, ordena de forma decrescente
    """

    df = metrics_df.copy()

    # --- Garantir que coluna "date" é datetime ---
    df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date  # 🔥 só a data

    # --- Filtro por data ---
    if start_date:
        start_date = pd.to_datetime(start_date).date()
        df = df[df["date"] >= start_date]

    if end_date:
        end_date = pd.to_datetime(end_date).date()
        df = df[df["date"] <= end_date]

    # --- Ordenação por coluna ---
    if order_by and order_by in df.columns:
        df = df.sort_values(by=order_by, ascending=not desc)

    # --- Controle de permissão ---
    if role != "admin" and "cost_micros" in df.columns:
        df = df.drop(columns=["cost_micros"])

    # --- Limit (pagina os resultados) ---
    if limit:
        df = df.head(limit)

    return df.to_dict(orient="records")
