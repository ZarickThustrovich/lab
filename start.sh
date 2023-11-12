venv/Scripts/activate
python manage.py runserver 127.0.0.1:8000
daphne lab.asgi:application -p 8001