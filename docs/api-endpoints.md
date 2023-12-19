# Конечные точки API

## **Первая версия**

Для доступа к первой версии в начале запроса устанавливается `/api/v1/`

### **Анкета**

#### `/questionnaire/list/ (GET)`

_Получение всех имеющихся анкет у авторизированного пользователя_

---

#### `/questionnaire/detail/<int:pk_questionnaire>/ (GET)`

_Получение детального обзора анкеты пользователя_

---

### **Авторизация и регистрация**

#### `/auth/create-user/ (POST)`

_Сервис для создания пользователя, его должностей и генерации анкет_

Пример получаемых данных:

```
data = {

    "username": "username",
    "password": "password",
    "first_name": "first_name",
    "last_name": "last_name",
    "patronymic": "patronymic",
    "user_positions": [
        {
            "department": department.id,
            "rate": rate.id,
            "position": position.id,
        },
        ...
    ],
    "questionnaire": [questionnaire.id, ...]

}
```

> user_positions и questionnaire являются необязательными, если эти данные будут пустые ([]), создастся только пользователь django

---
