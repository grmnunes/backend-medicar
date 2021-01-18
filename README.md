## Desafio Intmed - API Medicar
Backend do sistema para gestão de consultas em clínicas médicas - Medicar

## Rodando o projeto

1. Clone o repositório do projeto

```bash
https://github.com/grmnunes/test-intmed-app.git
```

2. Utilize o [pip](https://pip.pypa.io/en/stable/) para instalar as dependências com o comando: 
```bash
pip install -r requirements.txt
```
> O projeto utiliza o banco de dados SQLite.

3. Execute as **migrations** com o comando: 

```bash
python manage.py migrate
```

4. Crie o usuário administrador do sistema (**superusuario**) com o comando: 

```bash
python manage.py createsuperuser
```

5. Por fim, execute o sistema com o comando: 

```bash
python manage.py runserver
```
> O painel administrativo do sistema estará disponível em: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)


Recurso   | Endpoint | Métodos HTTP aceitos
--------- | ---------|-----------
Cadastro | [/registration](http://127.0.0.1:8000/rest-auth/registration/)| POST
Login | [/login](http://127.0.0.1:8000/rest-auth/login/)|POST
Especialidades| [/api/v1/especialidades](http://127.0.0.1:8000/api/v1/especialidades)| GET
Médicos| [/api/v1/medicos](http://127.0.0.1:8000/api/v1/medicos)|GET
Agendas| [/api/v1/agendas](http://127.0.0.1:8000/api/v1/medicos)|GET
Consultas| [/api/v1/consultas](http://127.0.0.1:8000/api/v1/consultas)|GET, POST, DELETE

> Todas as rotas, exceto, as de cadastro e login, necessitam de autenticação.
