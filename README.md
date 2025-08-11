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

Repositório:
   ```bash
     https://github.com/Nicolas-So06/ProjetoEmprestimo.git