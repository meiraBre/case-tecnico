from fastapi import APIRouter
from database.db import get_engine
from sqlalchemy import text
import pandas as pd

metrics_router = APIRouter(prefix="/metrics", tags=["metrics"])

ALLOWED_ORDER_COLS = {
    "account_id", "campaign_id", "cost_micros", "clicks", "conversions",
    "impressions", "interactions", "date" 
}

@metrics_router.get("/")
def get_metrics(
    role: str,
    order_by: str = None,
    start_date: str = None,  # formato YYYY-MM-DD
    end_date: str = None,    # formato YYYY-MM-DD
    limit: int = None,
    desc: bool = False
):
    """
    Lê direto do banco (tabela 'metricas'), aplica filtros/ordenação/limite
    e remove 'cost_micros' para quem não é admin.
    """

    engine = get_engine()

    # 1) Monta SQL base
    sql = "SELECT * FROM metricas WHERE 1=1"
    params = {}

    # 2) Filtros de data (deixe as colunas no formato YYYY-MM-DD no banco)
    if start_date:
        sql += " AND date >= :start_date"
        params["start_date"] = start_date
    if end_date:
        sql += " AND date <= :end_date"
        params["end_date"] = end_date

    # 3) Ordenação segura (só por colunas permitidas)
    if order_by and order_by in ALLOWED_ORDER_COLS:
        direction = "DESC" if desc else "ASC"
        sql += f" ORDER BY {order_by} {direction}"

    # 4) Limite
    if limit:
        sql += " LIMIT :limit"
        params["limit"] = int(limit)

    # 5) Executa e carrega em DataFrame (fica fácil de tratar tipos)
    with engine.connect() as conn:
        df = pd.read_sql_query(text(sql), conn, params=params)

    # 6) Normaliza 'date' como date (opcional, útil para o front)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.date

    # 7) Permissões: esconde cost_micros para não-admin
    if role != "admin" and "cost_micros" in df.columns:
        df = df.drop(columns=["cost_micros"])

    return df.to_dict(orient="records")