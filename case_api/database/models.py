from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False, unique=True)
    email = Column("email", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    role = Column("role", String)

    # Caso fosse necessário a criação de usuários
    def __init__ (self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

class Metrics(Base):
    __tablename__ = "metricas"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    account_id = Column("account_id", Integer)
    campaign_id = Column("campaign_id", Integer)
    cost_micros = Column("cost_micros", Float)
    clicks = Column("clicks", Float)
    conversions = Column("conversions", Float)
    impressions = Column("impressions", Float)
    interactions = Column("interactions", Float)
    date = Column("date", String)