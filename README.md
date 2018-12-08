## Para Instalar

Para instalar as dependências do projeto, executar:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations ou python manage.py makemigrations helloworld
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

## Para Executar

Para executar o Servidor de testes do Django, execute:

```bash
python manage.py runserver
