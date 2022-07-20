<h1> API для проекта YaTube</h1>
##Описание проекта API Yatube:
API, позволяющее аутентифицированным пользователям создавать, 
редактировать и удалять записи в социальной сети Yatube, а также просматривать 
и комментировать записи других пользователей и подписываться на других авторов. 

<h1>Стек:</h1>

    Django 2.2.16
    Python 3.7
    djoser 2.1
    django rest framework
    Django ORM
    Simple JWT

<h2>Мануал по устновке проекта</h2>

<h4><i>1.Клонировать репозиторий и перейти в него в командной строке:</i></h4>

    git clone https://github.com/TretyakovAnton/api_final_yatube.git

    cd api_final_yatube

<h4><i>2.Установить виртуальное окружение</i></h4>

    python -m venv venv

<h4><i>3.Запустить виртуальное окружение</i></h4>

    venv\Scripts\activate

<h4><i>4.Установить зависимости из файла requirements.txt:</i></h4>

    python -m pip install --upgrade pip

    pip install -r requirements.txt

<h4><i>5.Выполнить миграции:</i></h4>

    python manage.py migrate

<h4><i>6.Запустить проект:</i></h4>

    python manage.py runserver
      
<h1>Примеры запросов</h1>

- GET-Response: http://127.0.0.1:8000/api/v1/posts/ 

        Request:
        [ { 'id': 1, 
        'author': 'author', 
        'image':'' 'text': 
        'text', 'pub_date': 
        'pub_date', 
        'group': null }, ]

- POST-Response: http://127.0.0.1:8000/api/v1/posts/ :

        {
           "text": "string",
           "image": "string",
           "group": 0
        }

        Request:

        {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2019-08-24T14:15:22Z",
        "image": "string","group": 0
        }


- Остальные возможные запросы можно посмотреть 

        http://127.0.0.1:8000/redoc/