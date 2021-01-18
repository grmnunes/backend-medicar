## Desafio Intmed - API Medicar
Backend do sistema para gestão de consultas em clínicas médicas - Medicar

## Rodando o projeto

1. Clone o repositório do projeto

```bash
git clone https://github.com/grmnunes/backend-medicar.git
```

2. Utilize o [pip](https://pip.pypa.io/en/stable/) para instalar as dependências com o comando: 
```bash
pip install -r requirements.txt
```
> O projeto utiliza o banco de dados SQLite.

3. Crie as **migrations** com o comando: 

```bash
python manage.py makemigrations
```

4. Execute as **migrations** com o comando: 

```bash
python manage.py migrate
```

5. Crie o usuário administrador do sistema (**superusuario**) com o comando: 

```bash
python manage.py createsuperuser
Ou
winpty python manage.py createsuperuser (*Caso esteja em utilizando o gitbash*)
```

6. Por fim, execute o sistema com o comando: 

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
## Cadastro
```javascript
{
	"name": "Joao",
	"username": "joao",
	"email": "joao@email.com",
	"password1": "12345678&&",
	"password2": "12345678&&"
} 
```
## Login
```javascript
{
	"username": "joao",
	"password": "12345678&&"
	
}
```
## Marcar consulta
```javascript
{
	"agenda_id": 1,
	"horario": "22:00"
}
```
