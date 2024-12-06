# Тестовое задание

## Установка зависимостей:

`pip install -r requirments.txt`

## Структура проекта:
Папка locators содержит локаторы элементов на страницах

Папка pages содержит локаторы элементов на страницах

Папка tests содержит тесты страниц

## Параметры:

Браузер - Google Chrome

Разрешение - 1920х1080

## Запуск тестов с формированием отчета в Allure:
`pytest  -v -s  --alluredir allure_results`

## Просмотр отчета в Allure:

`pytest  -v -s  --alluredir allure_results`
