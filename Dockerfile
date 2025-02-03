# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl

# Устанавливаем poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости проекта
RUN /root/.local/bin/poetry install

# Применяем миграции и собираем статические файлы
RUN /root/.local/bin/poetry run python manage.py migrate
RUN /root/.local/bin/poetry run python.manage.py collectstatic --noinput

# Указываем команду для запуска сервера
CMD ["/root/.local/bin/poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "Mahiru_Homework_REST_API.wsgi:application"]
