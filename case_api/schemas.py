from pydantic import BaseModel

# --- Modelo para o corpo do login ---
class LoginData(BaseModel):
    email: str
    password: str