# Projeto ErickGym


### Endpoints API:


#### Root:
<https://erickgym-server-latest.onrender.com/>


#### Exercicios

|  METHOD  |        PATH         | BODY            | DATA        | STATUS CODE      | DESCRIÇÃO              |
| :------: |  ------------------ | --------------- | ----------- | ---------------- | ---------------------- |
| POST     | /api/r/exercicios/    | Dados-Exercicio | Exercício   | 201 (CREATED)    | Criar-novo-Exerícios   |
| GET      | /api/r/exercicios/    | ---             | [Exercicio] | 200 (OK)         | Lista-Exercícios       |
| GET      | /api/r/exercicios/:id | ---             | [Exercicio] | 200 (OK)         | Lista-Exercício        |
| PUT      | /api/r/exercicios/:id | Dados-Exercício | ---         | 204 (NO CONTENT) | Atualizar-Exercício    |
| DELETE   | /api/r/exercicios/:id | ---             | ---         | 204 (NO CONTENT) | Deletar-Exercício      |


#### Alunos
|  METHOD  |        PATH         | BODY            | DATA        | STATUS CODE      | DESCRIÇÃO              |
| :------: |  ------------------ | --------------- | ----------- | ---------------- | ---------------------- |
| POST     | /api/r/alunos/        | Dados-Alunos    | Alunos      | 201 (CREATED)    | Criar-novo-Aluno       |
| GET      | /api/r/alunos/        | ---             | [Alunos]    | 200 (OK)         | Lista-Alunos           |
| GET      | /api/r/alunos/:id     | ---             | [Alunos]    | 200 (OK)         | Dados-Aluno            |
| PUT      | /api/r/alunos/:id     | Dados-Alunos    | ---         | 204 (NO CONTENT) | Atualizar-Aluno        |
| DELETE   | /api/r/alunos/:id     | ---             | ---         | 204 (NO CONTENT) | Deletar-Aluno          |
