<h1 align="center">Aplicação Web para Visualização de Dados de Performance</h1>

## 📌 Introdução
Projeto (para um case técnico) desenvolvido entre os dias **19 e 26 de agosto**. Este case técnico envolve:

- Criação de uma API em Python com FastAPI
- Banco de dados utilizando SQLAlchemy e SQLite
- Controle de versões com Alembic
- Front-end básico com página de login e dashboard
- Funcionalidades de filtro e ordenação de dados

## ✅ Requisitos Funcionais

- [x] Sistema de login por email e senha
- [x] Exibição de dados em formato tabelar no frontend
- [x] Filtro de dados por data
- [x] Ordenação por qualquer coluna
- [x] Exibição da coluna `cost_micros` apenas para usuários com papel `admin`

## ⚙️ Requisitos Não Funcionais

- [x] API escrita em Python

## 🧰 Tecnologias Utilizadas

- **API**: Python, FastAPI(framework para criar API em python), Pandas(para manipular os arquivos CSV), Uvicorn(servidor ASGI).
- **Backend**: SQLAlchemy, SQLite, Alembic(para controle de versões do banco de dados).
- **Frontend**: HTML, CSS, JavaScript.
- **Organização**: Notion (para organização de tarefas diárias e metas para entregar o case dentro do prazo).
- **Suporte**: ChatGPT para auxílio em bugs e melhorias. 

## 🚀 Como Executar o Projeto

1. **Baixar o arquivo `metrics.csv`**  
   Disponível em: [Google Drive](https://drive.google.com/drive/folders/1wvkKhZcoikv4z4l40LCoj4-YVowotmQp?usp=drive_link)  
   Coloque na pasta `case_api`.

2. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt

3. **Criar o banco de dados**:
    ```bash
    alembic upgrade head

4. **Popular o banco com dados iniciais**:
    ```bash
    python data.py

5. **Rodar a API**:
    ```bash
    uvicorn main:app --reload

- A API estará disponível em: http://127.0.0.1:8000 Documentação interativa: http://127.0.0.1:8000/docs

6. **Rodar o Frontend Abra os arquivos HTML diretamente no navegador**:
- Página de Login → frontend/login.html
- Página de Dashboard → frontend/dashboard.html
- Login Utilize os usuários já cadastrados no arquivo users.csv

## 🗂️ Estrutura do Projeto
```bash
case_api/
├── alembic/                  # Migrações do banco de dados
├── database/                 # Conexão, models e scripts relacionados ao DB
│   ├── banco.db
│   ├── db.py
│   ├── models.py
│   └── alembic.ini
├── data.py                   # Script seed/manipulação de dados
├── login_routes.py           # Rotas de login
├── main.py                   # Inicialização da aplicação FastAPI
├── metrics_routes.py         # Rotas para métricas
├── metrics.csv               # Arquivo CSV de métricas
├── schemas.py                # Schemas Pydantic
├── users.csv                 # Arquivo CSV de usuários
├── frontend/                 # Arquivos do front-end
│   ├── dashboard.css
│   ├── dashboard.html
│   ├── dashboard.js
│   ├── login.css
│   ├── login.html
│   └── login.js
├── img/                      # Imagens usadas no front-end
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação do projeto
└── .gitignore                # Arquivos/pastas ignorados pelo Git
```

## 💡 Possíveis Melhorias Futuras
- Implementar login com JWT e autenticação por token
- Armazenar senhas com hash no banco de dados
- Migrar banco para servidor dedicado
- Reestruturar o visual da página para refletir melhor a identidade da empresa
- Colocar uma opção para o próprio usuário selecionar a quantidade de itens (linhas das colunas) que deseja visualizar na página

## 📚 Referências
- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Curso de FastAPI e Backend Completo](https://www.hashtagtreinamentos.com/curso-de-fastapi-python)

## ⚠️ Aviso
Este projeto foi desenvolvido exclusivamente para fins de estudo e avaliação técnica durante um processo seletivo.
Não possui vínculo oficial com nenhuma empresa.

## 📞 Contato
Brenda Meira 
- 🔗[LinkedIn](https://www.linkedin.com/in/meirabrenda540/)
- Email: bremeirah@gmail.com
