# Проектная работа 9 спринта

Ссылка на проект: https://github.com/iliazaraysky/ugc_sprint_2

## Github workflows

1. В проекте настроен Github workflows. После каждого pull,
проект проверяется на трех версиях Python (3.7, 3.8, 3.9)
2. Создаются отчеты для Flake8 и mypy
3. Отчет, при успешной загрузке отправляется в Telegram, для этого был выбран
action = appleboy

## Анализ хранилищ
Сравниваю производительность MongoDB и Elasticsearch в операциях **вставки/поиска**
в разделе [data_storage_testing](data_storage_testing)

1. Переходим в папку
2. Запускаем docker-compose.yml
3. Тесты доступны через Jupyter Notebook в папке data
4. Результаты в [data_storage_testing/README.md](data_storage_testing/README.md)

## Clickhouse

Кластер из 3-х шардов по 3 реплики в папке [ugc_api/clickhouse/data_exercise](ugc_api/clickhouse/data_exercise)

1. Запустить проект можно файлом **docker-compose.yml** из папки [ugc_api/clickhouse/data_exercise](ugc_api/clickhouse/data_exercise)
2. Открыть Jyputer Notebook по ссылке из командной строки
3. В папке **config** лежит файл **.ipynb**

## Auth сервис

Для проведения полноценного тестирования был добавлен сервис аутентификации

После запуска Docker-compose проходим делаем POST-запрос для получения токенов:

Тело запроса:

```
{
    "login": "admin",
    "password": "password123"
}
```

Адрес запроса:

```
http://127.0.0.1/auth/v1/login
```

## MongoDB + FastAPI
В проект добавлен MongoDB. Действия пользователя, такие как комментарии, лайки,
записываются в MongoDB

Пример POST-запроса от пользователя, чтобы поставить фильму лайк
```
# Адрес запроса
127.0.0.1:8000/api/v1/films/user-event/add-like
```
```
{
    "film_id": "49a94bc3-4678-49e1-9dbf-6386bb7c21d2",
    "user_id": "f354d652-6cec-4925-96c1-802f7b22844c",
    "like": true
}
```

Получить все лайки можно отправив GET-запрос на адрес

```
127.0.0.1:8000/api/v1/films/user-event/get-likes
```
## Логи
В проекте логирование осуществляется в Logstash.

Удобный просмотр логов в Kibana адресу
```
127.0.0.1:5601
```
Для отображения логов в Kibana требуется завести Index Pattern

Чтобы завести паттерн, перейдите в Management → Stack Management → Index Patterns и нажмите Create index pattern.

После создания паттерна перейдите в Kibana → Discover, чтобы посмотреть содержимое индексов.
