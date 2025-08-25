import pandas as pd
from sqlalchemy import create_engine

def load_data():
    DATABASE_URL = "sqlite:///database/banco.db"
    engine = create_engine(DATABASE_URL)

    # Inserir usuários
    df_users = pd.read_csv("users.csv")
    df_users.to_sql("usuarios", engine, if_exists="append", index=False)
    
    # Inserir métricas
    df_metrics = pd.read_csv("metrics.csv")
    df_metrics.to_sql("metricas", engine, if_exists="append", index=False)

if __name__ == "__main__":
    load_data()
    print("✅ Dados inseridos com sucesso!")


