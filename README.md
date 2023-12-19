<table align="center"><tr><td align="center" width="9999">

<img width="200" src="public/logo-rsue.svg">

# РППС

Веб-приложение для рейтинга преподавателей РГЭУ (РИНХ)

</td></tr></table>

### Необходимые зависимости для запуска проекта:

- Python (3.7 и выше)
- poetry
- Node.js (12.15 и выше)
- yarn
- Make
- [GTK3](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer)

### Разработка

1. `make install` - установка необходимых зависимостей и настроек проекта

- Установка всех зависимостей Python и Node.js
- Создание .env файла с переменными окружения
- Создание базы данных SQLite
- Применение миграций для базы данных
- Сооздание дефолтного администратора (Логин и пароль: admin)

2. `make run` - запуск серверов разработки

- Django сервер (localhost:8000)
- Quasar сервер (localhost:8080)
- Mkdocs сервер (localhost:3000)

> Далее перейдите по адресу http://localhost:3000/, для изучения подробной документации, либо без запуска сервера в директории docs/
