## Run project:

1. Create and run virtual env:
```
python3.10 -m venv .env
source .env/bin/activate
```

2. Install requirements:
```
pip install -r requirements.txt
```

3. Run PostgreSQL with docker-compose:
```
docker-compose up
```

4. Apply migrations and run project:
```
pythn manage.py migrate
pythn manage.py runserver
```
