# Результат сравнения двух хранилищ MongoDB и elasticsearch

Все тесты доступны через **docker-compose.yml**

1. Запускаем docker-compose:

`docker-compose -f docker-compose.yml up --build`

2. После успешной сборки контейнеров будет доступна ссылка по адресу http://127.0.0.1/

3. Jupyter notebook файл находится в папке **data**

## Итоги тестов
### Вставка
Вставка 15 000 строк данных в MongoDB: 0:00:12

Вставка 15 000 строк данных в Elasticsearch: 0:01:20

### Поиск
Поиск по массиву данных размером в 15 000 строк. MongoDB: 0:00:10

Поиск по массиву данных размером в 15 000 строк. Elasticsearch: 0:00:20

