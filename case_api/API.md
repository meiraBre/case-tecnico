# 📌 Case Técnico - API de Métricas

## Índice
1. [Contextualização](#contextualização)  
2. [Passo a passo da construção da API e ferramentas utilizadas](#passo-a-passo-da-construção-da-api-e-ferramentas-utilizadas)  
3. [Resolução da questão do arquivo CSV grande](#resolução-da-questão-do-arquivo-csv-grande)  
4. [Requisitos funcionais e não funcionais da API](#requisitos-funcionais-e-não-funcionais-da-api)  
5. [Documentação dos endpoints](#documentação-dos-endpoints)  
6. [Como rodar a API](#como-rodar-a-api)  
7. [Como testar a API](#como-testar-a-api)  
8. [Utilização de IA](#utilização-de-ia)  
---

## Contextualização
#### A área de engenharia desempenha um papel crucial no desenvolvimento de software e na criação de soluções tecnológicas tanto para os clientes quanto para a empresa. Este case técnico propõe a construção construir uma aplicação web para gestores de uma agência de Marketing Digital, onde serão exibidos dados de performance de diversas contas da agência. Nesse arquivo explico como foi a construção da API e como você pode utilzar.
---

## 1. Passo a passo da construção da API e ferramentas utilizadas

### Passo 1 - Estrutura inicial do projeto
* Criar pasta do projeto: `case_api/`
* Criar arquivo principal: `main.py`
* Adicionar arquivos CSV: `users.csv` e `metrics.csv`

### Passo 2 - Instalar dependências
```bash
pip install fastapi uvicorn pandas python-multipart
```
* **fastapi** → framework da API
* **uvicorn** → servidor para rodar a API
* **pandas** → para manipulação de arquivos CSV
* **python-multipart** → necessário para aceitar formulários (ex: login via POST)

### Passo 3 - Criar a API básica (`main.py`)
* Implementar endpoints de **login**, **consulta de métricas** e **filtros**.

### Passo 4 - Rodar a API
```bash
uvicorn main:app --reload
```
* Documentação Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Documentação ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
---

## 2. Resolução da questão do arquivo CSV grande
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

#### ⚠️ **Alternativa**: em um projeto real, poderia-se utilizar **banco de dados** (ex: PostgreSQL, MySQL) ou **armazenamento em nuvem** (ex: S3) em vez de CSV.
---

## 3. Requisitos da API

### Requisitos funcionais
* Autenticação de usuários por **email** e **senha**.
* Consulta de métricas de campanhas.
* Filtragem por parâmetros (ex: `account_id`, `campaign_id`).

### Requisitos não funcionais
* A API deve ser escrita em python.
---

## 4. Documentação dos Endpoints

### 🔑 Autenticação

**POST** `/login`

* **Body (form-data):**

  ```json
  {
    "username": "admin@example.com",
    "password": "senha123"
  }
  ```
* **Resposta:**

  ```json
  {
    "access_token": "<token>",
    "token_type": "bearer"
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

## 5. Como rodar a API

### Pré-requisitos
* Python 3.9+
* Dependências instaladas (`pip install -r requirements.txt`)
* Arquivos `users.csv` e `metrics.csv` dentro de `case_api/`

### Executando
```bash
uvicorn main:app --reload
```
Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### CSV

* Baixe `metrics.csv` pelo link do Google Drive: [📂 metrics.csv](https://drive.google.com/drive/folders/1wvkKhZcoikv4z4l40LCoj4-YVowotmQp?usp=sharing)
---

## 6. Como testar a API

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

## 7. Utilização de IA

A API foi desenvolvida com o suporte de **IA (ChatGPT)** para auxílio em boas práticas de organização, escrita de documentação e estruturação do código. Todo o código e decisões técnicas foram validados manualmente.
---


