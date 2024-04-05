# Projeto ErickGym


### Endpoints API:


#### Root:
<https://erickgym-server-latest.onrender.com/>


#### Exercicios

|  METHOD  |        PATH         | BODY            | DATA        | STATUS CODE      | DESCRIÇÃO              |
| :------: |  ------------------ | --------------- | ----------- | ---------------- | ---------------------- |
| POST     | /api/exercicios/    | Dados-Exercicio | Exercício   | 201 (CREATED)    | Criar-novo-Exerícios   |
| GET      | /api/exercicios/    | ---             | [Exercicio] | 200 (OK)         | Lista-Exercícios       |
| GET      | /api/exercicios/:id | ---             | [Exercicio] | 200 (OK)         | Lista-Exercício        |
| PUT      | /api/exercicios/:id | Dados-Exercício | ---         | 204 (NO CONTENT) | Atualizar-Exercício    |
| DELETE   | /api/exercicios/:id | ---             | ---         | 204 (NO CONTENT) | Deletar-Exercício      |


#### Alunos
|  METHOD  |        PATH         | BODY            | DATA        | STATUS CODE      | DESCRIÇÃO              |
| :------: |  ------------------ | --------------- | ----------- | ---------------- | ---------------------- |
| POST     | /api/alunos/        | Dados-Alunos    | Alunos      | 201 (CREATED)    | Criar-novo-Aluno       |
| GET      | /api/alunos/        | ---             | [Alunos]    | 200 (OK)         | Lista-Alunos           |
| GET      | /api/alunos/:id     | ---             | [Alunos]    | 200 (OK)         | Dados-Aluno            |
| PUT      | /api/alunos/:id     | Dados-Alunos    | ---         | 204 (NO CONTENT) | Atualizar-Aluno        |
| DELETE   | /api/alunos/:id     | ---             | ---         | 204 (NO CONTENT) | Deletar-Aluno          |
