# 📌 Case Técnico - API 

## Índice
1. [Contextualização](#contextualização)  
2. [Passo a passo da construção da API e ferramentas utilizadas](#passo-a-passo-da-construção-da-api-e-ferramentas-utilizadas)  
3. [Resolução da questão do arquivo CSV grande](#resolução-da-questão-do-arquivo-csv-grande)  
4. [Requisitos funcionais e não funcionais da API](#requisitos-funcionais-e-não-funcionais-da-api)  
5. [Documentação dos endpoints](#documentação-dos-endpoints)   
6. [Como testar a API](#como-testar-a-api)   
---

## Contextualização
- A área de engenharia desempenha um papel crucial no desenvolvimento de software e na criação de soluções tecnológicas tanto para os clientes quanto para a empresa. Este case técnico propõe a construção construir uma aplicação web para gestores de uma agência de Marketing Digital, onde serão exibidos dados de performance de diversas contas da agência. Nesse arquivo explico como foi a construção da API e como você pode testa-la.
---

## Passo a passo da construção da API e ferramentas utilizadas

### Passo 1 - Estrutura inicial do projeto
* Criar pasta do projeto: `case_api/`
* Criar arquivo principal: `main.py`  Para inicialização da aplicação FastAPI
* Criar os outros arquivos para melhor organização
* Adicionar arquivos CSV: `users.csv` e `metrics.csv`
* Depois de ter criado o banco de dados e populado ele com os dados dos arquivos CSV conectar com a API `db.py`

### Passo 2 - Instalar dependências
```bash
pip install fastapi uvicorn pandas python-multipart
```
* **fastapi** → framework da API
* **uvicorn** → servidor para rodar a API
* **pandas** → para manipulação de arquivos CSV
* **python-multipart** → necessário para aceitar formulários (ex: login via POST)

### Passo 3 - Criar a API básica (`login_routes.py` e `metrics_routes.py`)
* Implementar endpoints de **login**, **consulta de métricas** e **filtros**.

### Passo 4 - Rodar a API
```bash
uvicorn main:app --reload
```
* Documentação Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Documentação ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
---

## Resolução da questão do arquivo CSV grande
Para evitar subir arquivos grandes no repositório:

1. Criar um `.gitignore` com:

   ```gitignore
   __pycache__/
   *.pyc
   case_api/metrics.csv
   ```
2. Remover o CSV do Git sem apagar localmente:

   ```bash
   git rm --cached case_api/metrics.csv
   git add .gitignore
   git commit -m "Remover CSV grande e adicionar .gitignore"
   git push origin dev
   ```
3. Disponibilizar o CSV no Google Drive:

   * [📂 Link para metrics.csv](https://drive.google.com/drive/folders/1wvkKhZcoikv4z4l40LCoj4-YVowotmQp?usp=sharing)

---

## Requisitos da API

### Requisitos funcionais
* Autenticação de usuários por **email** e **senha**.
* Consulta de métricas de campanhas.
* Filtragem por parâmetros (ex: `account_id`, `campaign_id`).

### Requisitos não funcionais
* A API deve ser escrita em python.
---

## Documentação dos Endpoints

### 🔑 Autenticação

**POST** `/login`

* **Body (form-data):**

  ```json
  {
    "username": "admin@example.com",
    "password": "senha123"
  }
  ```

### 📊 Métricas

**GET** `/metrics`

* **Parâmetros opcionais:** `account_id`, `campaign_id`
* **Resposta (exemplo):**

  ```json
  [
    {
      "account_id": 123,
      "campaign_id": 456,
      "cost_micros": 100000,
      "clicks": 10,
      "conversions": 2,
      "impressions": 500
    }
  ]
  ```

---

## Como testar a API

### Usando navegador

* Acesse Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Usando Postman 
- Abra o Postman.
- Adicione a URL base da API: http://127.0.0.1:8000
- Escolha o endpoint desejado (exemplo: /login ou /metrics).
- Configure o método HTTP correto (GET, POST, etc.).
- Se for um POST (como no login), vá em Body → form-data ou x-www-form-urlencoded e insira os parâmetros necessários, por exemplo:
 ```bash 
    username (email)
    password
```
- Clique em Send.
- Veja a response em formato JSON exibida no painel de resposta do Postman.
---



