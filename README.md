# Тестовое задание

## Начало работы с приложением

### 1. Создание и активация Виртуального окружения (При необходимости)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения (.env)

**Пример** содержания файла *.env*

```
# Настройка Базы данных
DB_NAME=TestStud
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Подключение Redis
REDIS_LOCATION=redis://:your_password_here@localhost


# Настройка электронной почты для отправки сообщений
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=youremail@example.com
EMAIL_HOST_PASSWORD=yourpassword
DEFAULT_FROM_EMAIL=youremail@example.com


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

## Использование приложения (Эндпоинты)

- **GET** /courses/stats/ - Выводит Статистику по курсам>

- **GET** /courses/ - Выводит список курсов


- **GET** /courses/id/ - Выводит информацию о курсе в JSON формате

- **PATCH** /courses/id/ - Позволяет внести изменения в информацию о курсе
    - **name**: Название курса
    - **start_date**: Дата начала
    - **end_date**: Дата окончания
    - **lectures_count**: Количество лекций

- **DELETE** /courses/id/ - Удаляет курс


- **GET** students/ - Список студентов
- **GET** students/id/ - Информация о студенте в JSON формате
- **PATCH** /students/id/ - Позволяет внести изменения в информацию о студенте
    - **name**: ФИО студента
    - **birth_day**: Дата рождения студента

- **DELETE** /students/id/ - Удаляет студента


- **GET** /send_message/ - Форма для отправки сообщения на почту
