# Código Inicial para a Tarefa de REST APIs com FastAPI
# Execute com: uvicorn main:app --reload
# (salve este arquivo como main.py)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de Livros")

# Dados iniciais em memória
books = [
    {"id": 1, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899, "genre": "Ficção"},
    {"id": 2, "title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011, "genre": "História"},
    {"id": 3, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "genre": "Programação"},
]


# Tarefa 1: Criar a Primeira Rota
# Defina a rota GET /books que retorna a lista de livros
# Dica: use @app.get("/books")


# Tarefa 2: Buscar Livros por ID e Filtrar por Gênero
# Defina GET /books/{book_id} e adicione o parâmetro opcional `genre` em GET /books
# Dica: para o 404, use raise HTTPException(status_code=404, detail="Livro não encontrado")


# Tarefa 3: Cadastrar Livros com Validação
# Defina o modelo Pydantic BookCreate e a rota POST /books com status_code=201
class BookCreate(BaseModel):
    # Declare os campos: title, author, year e genre
    pass
