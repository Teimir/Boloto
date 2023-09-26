# Boloto

## Установка
### Нужные библиотеки:
python -m pip install Django 
python -m pip install Pillow

### Сборка статиков и миграция:
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

## Ручной запуск: 
python3 manage.py runserver

## Запуск в Докере: 
sudo tmux at -t 0
docker-compose up --build
