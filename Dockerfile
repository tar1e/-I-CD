# Используем официальный Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Открываем порт Flask
EXPOSE 5000

# Команда запуска приложения
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
