# Desafio Lacrei Saúde Back-end: Desenvolvendo uma API para Gerenciamento de Consultas Médicas

## Introdução

> API desenvolvida com Django e Django Rest Framework para o desefio back-end da instituição Lacrei Saúde.

## Arquitetura

> Para esta aplicação, três tabelas foram criadas, buscando a normalização do banco de dados. A tabela "Professional" herda da classe "AbstractUser", mas com informações adicionais como Nome Social e Profissão. A tabela Address é um complemento às informações do Profissional recebendo a chave estrangeira dessa tabela. Por fim, a tabela Visit, onde estarão agendadas as consultas para os profissionais.

> Para as views, herdei a Classe ModelViewSet buscando acelerar o desenvolvimento, já que esta tras um CRUD completo para a model. Entretanto foi necessário reescrever os métodos create e partial_update da ModelViewSet de Professional, pois tanto para criar quanto editar, o enderesso pode estar no corpo da requisição. Além disso, uma view extra foi criada para Visit.

> Visando a facilidade de teste e uso, mantive o banco de dados sqLite, cujo pode ser facilmente removido após os testes.

> Alguns testes foram escritos para o app Visit. 

> Abaixo estão as informações de como rodar a aplicação e os testes.

## Preparando do ambiente

 1. Faça do clone deste repositório para a sua máquina;
 2. Acesse a pasta do repositório;
 3. Crie um ambiente virtual com o comando `python3 -m venv venv`;
 4. Ative o ambiente virtual `source venv/bin/activate` pelo linux ou `venv/Scripts/activate` no Windows;
 5. Instale as dependências com o comando: `pip install -r requirements.txt`;
 6. Rode as migrações para obanco de dados com o comando: `python manage.py migrate`;
 7. Inicie o servidor com o comando: `python manage.py runserver`;
 8. Há um aquivo chamado "test.http" na raiz do projeto, se estiver usando o VSCode, pode instalar uma extensão chamadas "REST Client" e usar as requisitções do aquivo, ou pode usar outra ferramenta de requisição como Postman ou Insominia. 

## Rodando os testes
Com o ambiente virtual ativado rode o comando: `python manage.py test`


## Funcionalidades e exemplos:

**Cadastro de Profissional:**
Permite criar novos profissionais de saúde por meio de uma requisição POST.

***Exemplo de requisição POST:***

POST http://localhost:8000/api/professional/   
Content-Type: application/json

```json
{
    "first_name": "test",
    "last_name": "test",
    "username": "test",
    "email": "test@mail.com",
    "password": "123",
    "profession": "Doctor",
    "address": {
        "street": "Rua dos bobos",
        "number": 0,
        "complement": "esquina",
        "city": "De Deus",
        "state": "SP",
        "zip_code": "11111-111",
        "neighborhood": "Centro"
    }
}
```

**Edição de Profissional:**

Permite modificar os dados de um profissional já cadastrado por meio de uma requisição PATCH. A requisição deve especificar o identificador único (ID) do profissional na URL e conter os dados que deseja alterar no corpo da requisição.

***Exemplo de requisição PATCH:***

PATCH http://localhost:8000/api/professional/{professional ID}/     
Content-Type: application/json

```json
{
    "profession": "Psycologist"
}
```

**Exclusão de Profissional:**

Permite excluir um profissional cadastrado por meio de uma requisição DELETE. A requisição deve especificar o identificador único (ID) do profissional na URL.

***Exemplo de requisição DELETE:***

DELETE http://localhost:8000/api/professional/{professional ID}/   

**Recuperar Profissional (por ID):**
Permite recuperar os dados de um profissional específico por meio de uma requisição GET. A requisição deve especificar o identificador único (ID) do profissional na URL.

***Exemplo de requisição GET:***

GET http://localhost:8000/api/professional/{professional ID}/ 

**Listar Todos os Profissionais:**
Permite recuperar uma lista de todos os profissionais cadastrados no sistema por meio de uma requisição GET.

***Exemplo de requisição GET:***

GET http://localhost:8000/api/professional/


**Marcar Consulta:**
Permite registrar uma nova consulta médica na agenda de um profissional por meio de uma requisição POST.

***Exemplo de requisição POST:***

POST http://localhost:8000/api/visit/   
Content-Type: application/json

```json
{
    "date": "2024-07-09 09:00:00",
    "professional": "ef0dc211-94bd-458f-bb2d-a36dde69777e"
}
```

**Reagendar Consulta:**
Permite alterar a data e hora de uma consulta já agendada através de uma requisição PATCH.

***Exemplo de requisição PATCH:***

PATCH http://localhost:8000/api/visit/{visit ID}/   
Content-Type: application/json

```json
{
    "date": "2024-07-09 09:00:00",
}
```
**Deletar Consulta:**

Permite deletar uma consulta agendada através de uma requisição DELETE.


***Exemplo de requisição POST:***

DELETE http://localhost:8000/api/visit/{visit ID}/


**Listar Agenda de um Profissional:**
Permite listar as consultas de um profissional através de uma requisição GET.

***Exemplo de requisição GET:***

GET http://localhost:8000/api/visit/get_by_professional?professional={professional ID}/  
Content-Type: application/json
