# Сайт "Афиша интересных мест в Москве"
Интерактивная карта Москвы, на которой отображены известные виды активного отдыха с подробным описанием.

Front-end часть является частью учебного проекта и взята из [репозитория](https://github.com/devmanorg/where-to-go-frontend) Devman.

## Пример работы сайта
Посмотреть пример работы сайта можно посмотреть на [pythonanywhere.com](http://kawabanga.pythonanywhere.com/)

## Используемые библиотеки

-   [Django](https://www.djangoproject.com/)  — фреймворк для веб-приложений.
-   [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/index.html)  — это приложение Django для сортировки объектов с помощью drag-and-drop в списках и интерфейсе администратора Django.
-   [django-tinymce](https://github.com/jazzband/django-tinymce)  — это приложение Django, содержащее виджет для отображения поля формы в качестве WYSIWYG-редактора TinyMCE.


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` и запишите туда данные в формате `ПЕРЕМЕННАЯ=значение`.

- `DEBUG`  — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY`  — секретный ключ проекта.
- `ALLOWED_HOSTS`  — смотри  [документацию Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).

## Образец JSON-файла с локациями

```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d1.jpg",
        "https://kudago.com/media/images/place/d2.jpg",
        "https://kudago.com/media/images/place/d3.jpg"
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

## Запуск

 Клонируйте репозиторий с Github:
```shell
https://github.com/rudenko-ks/django-afisha-where-to-go.git
```
- Создайте виртуальное окружение:
```shell
python -m venv .venv
source .venv/bin/activate
```

- Установите зависимости командой:
```shell
pip install -r requirements.txt
```
    
- Создайте файл  `.env`  и внесите в него переменные окружения.
    
- Создайте файл базы данных и сразу примените все миграции командой:
```shell
python manage.py migrate
```
    
- Создайте администратора сайта в базе данных:
```shell
python manage.py createsuperuser
```
- Запустите сервер командой:
```shell
python manage.py runserver
```

## Наполнение сайта контентом

Чтобы загрузить на сайт больше данных необходимо выполнить команду `load_place` и в качестве аргумента передать ссылку на JSON файл.  Информация о новом месте будет добавлена в БД на сервер.

```shell
python manage.py load_place https://github.com/devmanorg/where-to-go-places/raw/master/places/Павильон%20«Космос»%20на%20ВДНХ.json
```

## Использование

Главная страница располагается по адресу http://localhost:8000/ отображает карту с интересными местами в Москве.

Выбрав локацию на карте можно увидеть подробное описание с фотографиями.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте  [Devman](https://dvmn.org/).

Тестовые данные взяты с сайта  [KudaGo](https://kudago.com/).
> Written with [StackEdit](https://stackedit.io/).
