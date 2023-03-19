# Новое русское вино
[![imageup.ru](https://imageup.ru/img89/4254182/chrome_ieffn8nzab.jpg)](https://imageup.ru/img89/4254182/chrome_ieffn8nzab.jpg.html)
Сайт магазина авторского вина "Новое русское вино".

## Подготовка к запуску проекта
В папку с проектом добавить файл `.env`.
Добавить следующе поля:
```
TEMPLATE_PATH='Путь к шаблону'
TEMPLATE_EXTENSIONS='Расширение для шаблоны'
TEMPLATE_NAME='Имя шаблона'
HOST_ADDRESS='Адрес где развенуть сайт'
HOST_PORT='Порт сайт'
```
Заполнить поля при необходимости нужными данными.
В коде программы указаны дефолтные значения. 

## Запуск проект

1. Установить зависимости,
```python
pip install requirements.txt
```
2. [Cкачать](https://dvmn.org/filer/canonical/1610450333/763/) тестову таблицу.
3. Передать два обязательных аргумента для запуска:
- Путь до таблицы
- Имя таблицы
``` python
python main.py --sheet_path='Путь до таблицы' --sheet_name='Имя файла'
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
