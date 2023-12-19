# Установка

### Необходимые инструменты для запуска

- Python (3.7 и выше)
- poetry
- Node.js (12.15 и выше)
- yarn
- Make
- [GTK3](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)
- Docker и docker-compose

> Docker и Docker-compose необходимы для запуска PostgreSQL в контейнере (настоятельно рекомендуем использовать PostgreSQL, так как данный инструмент используется на производстве, а мы стараемся придерживаться методологии ["12 факторов приложения"](https://12factor.net/ru/)).

### Команды запуска серверов разработки

После успешной установки всех инстурментов, запустим докер контейнер с базой данных. Данаая команда поднимет контейнер PostgreSQL

```
docker-compose up -d
```

Со следующими параметрами:

- POSTGRES_DB: "db_name"
- POSTGRES_USER: "db_user"
- POSTGRES_PASSWORD: "db_password"

> По дефолту, связь устанавливается с PostgreSQL в файле с переменными окружения - .env, для этого переменная USE_SQLITE далжна быть False и в DATABASE_URL, прописан путь до базы, например DATABASE_URL="pgsql://db_user:db_password@localhost:5432/db_name". НО! Если вы хотите использовать SQLite, установите USE_SQLITE=True (не забудьте про миграции).

Автоматическая установка всех зависимостей и настроек

```
make install
```

А именно:

- Установка всех зависимостей Python и Node.js
- Создание .env файла с переменными окружения
- Применение миграций для базы данных
- Сооздание дефолтного администратора (Логин и пароль: admin)

Запуск серверов разработки

```
make run
```

- Django сервер (localhost:8000)
- Quasar сервер (localhost:8080)
- Mkdocs сервер (localhost:3000)
