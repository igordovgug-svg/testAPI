# Blog API

REST API для блогу побудований на Django REST Framework

## Технології
- Python 3.x
- Django REST Framework
- SQLite

## Функціонал
- CRUD для постів
- CRUD для коментарів
- Кастомні permissions (редагувати/видаляти може тільки автор)

## Як запустити
1. git clone https://github.com/igordovgug-svg/Blog-API-djangorest
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver

## API Endpoints

### Posts
- GET /api/v1/post/ — список всіх постів
- POST /api/v1/post/ — створити пост
- PUT /api/v1/post/{id}/ — оновити пост (тільки автор)
- DELETE /api/v1/postdelete/{id}/ — видалити пост (тільки автор)

### Comments
- GET  /api/v1/postcomment/ — список віх коментарів
- POST /api/v1/postcomment/ — додати коментар
- DELETE /api/v1/postcomment/{id}/ — видалити коментар (тільки автор)
