#Arquivo criado para facilitar a conexão da API com o Banco de dados
from sqlalchemy import create_engine

# Caminho do seu banco SQLite
DATABASE_URL = "sqlite:///database/banco.db"

# Para SQLite + FastAPI, use check_same_thread=False
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

def get_engine():
    return engine
