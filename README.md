# Тестовое задание

## Начало работы с приложением

### 1. Переход в директорию Students

``` bash
cd Students
```

### 2. Установка зависимостей

```commandline
pip install -r requirements.txt
```

### 3. Настройка переменных окружения (.env)

**Пример** содержания файла *.env*

```bash
# Настройка Базы данных
DB_NAME=TestStud
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Ключ для Хеширования пароля
SECRET_KEY=UNIQUE_RANDOM_STRING_OF_AT_LEAST_50_CHARACTERS
```

### 4. Миграция таблиц в базу данных

```bash
python manage.py migrate
```

### 5. Запуск приложения

```bash
python manage.py runserver
```
