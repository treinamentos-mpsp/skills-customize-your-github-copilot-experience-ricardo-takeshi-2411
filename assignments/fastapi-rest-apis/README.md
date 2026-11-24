# 📘 Assignment: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST com o framework FastAPI, criando rotas, recebendo parâmetros, validando dados com Pydantic e retornando respostas com os códigos HTTP corretos.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota

#### Descrição
Configure uma aplicação FastAPI e crie uma rota que retorne a lista de livros armazenada na variável `books`, usando o método HTTP `GET`.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` chamada `app`
- Definir a rota `GET /books` que retorne a lista completa de livros
- Iniciar o servidor com `uvicorn main:app --reload` e acessar `http://127.0.0.1:8000/docs` para ver a rota documentada automaticamente


### 🛠️ Buscar Livros por ID e Filtrar por Gênero

#### Descrição
Crie uma rota para buscar um livro específico pelo seu identificador e adicione um filtro opcional por gênero na listagem de livros.

#### Requisitos
O programa concluído deve:

- Definir a rota `GET /books/{book_id}` que retorne o livro com o `id` informado
- Retornar o status `404 Not Found` com a mensagem `"Livro não encontrado"` quando o `id` não existir (use `HTTPException`)
- Adicionar um parâmetro de consulta opcional `genre` em `GET /books`, para retornar apenas livros do gênero informado
- Exemplo de uso:

```text
GET /books?genre=Ficção
GET /books/2
```


### 🛠️ Cadastrar Livros com Validação

#### Descrição
Crie uma rota `POST /books` que receba os dados de um novo livro no corpo da requisição, valide esses dados com um modelo Pydantic e adicione o livro à lista.

#### Requisitos
O programa concluído deve:

- Criar um modelo Pydantic `BookCreate` com os campos `title` (texto), `author` (texto), `year` (inteiro) e `genre` (texto)
- Definir a rota `POST /books` que receba um `BookCreate` e adicione o livro à lista, gerando um `id` automaticamente
- Retornar o livro criado com o status `201 Created`
- Rejeitar automaticamente (status `422`) requisições em que `year` não seja um inteiro ou em que algum campo esteja ausente
- Testar o cadastro pela interface em `/docs`, verificando que o novo livro aparece em `GET /books`
