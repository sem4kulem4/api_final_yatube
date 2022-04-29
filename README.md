# api_final

---

### API YATUBE

Социальная сеть, в которой можно выкладывать посты, комментировать их,
вступать в группы по интересам и подписываться на публикации других пользователей
теперь и в виде API


---
### Как запустить проект:

Клонировать репозиторий:

```
git clone git@github.com:sem4kulem4/api_final_yatube.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
---
### Эндпоинты

Документация по проекту
```
/redoc/
```

Получение токена
```
api/v1/api-token-auth/
```
Список всех постов. Доступны offset и limit
```
api/v1/posts/
```
Методы GET, PUT, PATCH, DELETE поста по id
```
api/v1/posts/{post_id}
```
Список всех групп
```
api/v1/groups/
```
Информация о группе по ID
```
api/v1/groups/{group_id}/
```
Все комментарии с поста с post_id / Создание комментария к посту с post_id
```
api/v1/posts/{post_id}/comments/
```
Методы GET, PUT, PATCH, DELETE для комментария у поста с post_id
```
api/v1/posts/{post_id}/comments/{comment_id}/
```
Список подписок текущего пользователя. Доступен поиск
```
api/v1/follow/
```

### Об авторе
GitHub: https://github.com/sem4kulem4