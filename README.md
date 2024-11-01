# Сервис-помощник по приготовлению блюд
Этот проект представляет собой простой веб-сервис, который помогает пользователям находить рецепты и количество ингредиентов для их приготовления. Сервис предоставляет информацию о нескольких рецептах, включая омлет и пасту.

## Описание
Сервис позволяет получать список ингредиентов и их количество для приготовления различных блюд. Запросы к сервису могут содержать опциональный параметр servings, который указывает, на сколько порций нужно рассчитать количество ингредиентов.

## Примеры использования
Получение рецепта омлета на одну порцию:
- GET http://127.0.0.1:8000/omlet/

Ответ:
- яйца, шт: 2
- молоко, л: 0.1
- соль, ч.л.: 0.5
  
Получение рецепта омлета на 4 порции:
- GET http://127.0.0.1:8000/omlet/?servings=4
  
Ответ:
- яйца, шт: 8
- молоко, л: 0.4
- соль, ч.л.: 2.0

## Структура проекта
- calculator/views.py — файл, где хранится логика обработки запросов и переменная DATA с рецептами.
- urls.py — файл, где определяются маршруты для различных запросов к сервису.
