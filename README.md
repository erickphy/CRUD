# CRUD
Atividade avaliativa - Projeto CRUD de Entidades Relacionadas

# Projeto CRUD - Escola

## Tema do projeto
Sistema de gerenciamento de escola.

## Entidades
- **Aluno**
  - nome
  - matrícula
  - curso (relacionamento)
- **Curso**
  - id
  - nome
  - quantidade de vagas

## Relacionamento
Cada aluno pertence a um curso.  
O relacionamento é implementado no banco de dados e nas views.

## Estrutura de pastas
meu_crud/
├── app.py
├── bd/
│   └── escola.db
├── templates/
│   ├── index.html
│   ├── cursos.html
│   ├── novo_curso.html
│   ├── editar_curso.html
│   ├── alunos.html
│   ├── novo_aluno.html
│   └── editar_aluno.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js

## Como executar o projeto

1. Crie e ative o ambiente virtual:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instale as dependências:
   ```
   pip install flask flask_sqlalchemy
   ```
3. Execute o projeto:
   ```
   python app.py
   ```
4. Acesse [http://localhost:5000](http://localhost:5000) no navegador.

OBS: preciso indicar bem e verificar se realmente estou no diretório certo antes de executar o projeto, por isso digito isso:
cd "C:\Users\josee\Downloads\PROJETO CRUD\meu_crud"