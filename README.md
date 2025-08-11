# API de Gestão de Empréstimos

Este projeto é uma API RESTful completa para gerenciar itens emprestados entre amigos, construída com FastAPI e PostgreSQL.

## Visão Geral

O objetivo deste projeto é fornecer uma solução simples e eficiente para rastrear objetos que você empresta e pega emprestado, evitando esquecimentos. A API foi desenvolvida seguindo as melhores práticas de arquitetura de software, como a separação de concerns.

## Tecnologias Utilizadas

* **Backend:** Python 3, FastAPI
* **Banco de Dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Migrações:** Alembic
* **Validação de Dados:** Pydantic

## Funcionalidades

* CRUD completo para Amigos e Itens.
* Sistema de Empréstimos com ciclo de vida (status "ativo" e "devolvido").
* Endpoint de ação (`/devolver`) para lógica de negócio específica.
* Documentação interativa automática via Swagger UI (`/docs`).

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/Nicolas-So06/ProjetoEmprestimo.git
   python -m venv venv
   ```
2. Crie e ative um ambiente virtual:
   ```bash
    source venv/bin/activate  # No Linux/macOS
    # .\venv\Scripts\activate    # No Windows PowerShell
   
3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
   
4. Configure as variáveis de ambiente no arquivo .env.
5. Aplique as migrações do banco de dados:

    ```bash
    alembic upgrade head
   
6. Inicie o servidor:

    ```bash
    uvicorn app.main:app --reload
