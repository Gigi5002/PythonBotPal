# Telegram Bot Project

## Описание

Этот собой мой первый Telegram бот, который включает множество функциональных возможностей. Бот позволяет:
- Отправлять и изменять фотографии
- Отвечать на сообщения
- Показывать текущую погоду
- Работать с курсами валют
- Работать как полноценное веб-приложение
- Поддерживать различные способы оплаты
- Развертываться на сервере Render
- Использовать ngrok для туннелирования

Каждая функция реализована в отдельном файле, что упрощает управление и поддержку проекта.

## Требования

Для работы проекта необходимы следующие библиотеки и зависимости:
- `aiogram`
- `requests`
- `python-telegram-bot`
- `ngrok`
- И другие

## Установка

1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/telegram-bot-project.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd telegram-bot-project
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Создайте файл `.env` в корневой директории проекта и добавьте в него ваши токены и ключи:
    ```
    TELEGRAM_API_TOKEN=your_telegram_api_token
    WEATHER_API_KEY=your_weather_api_key
    ```

2. Запуск отдельных функций:

    - **Ответы на сообщения:**
        ```bash
        python functionality_bot.py
        ```
    - **Погода:**
        ```bash
        python weather_bot.py
        ```
    - **Курсы валют:**
        ```bash
        python currency_bot.py
        ```
    - **Веб-приложение:**
        ```bash
        python web_apps.py
        ```
    - **Бот написанный на aiogram:**
        ```bash
        python aiogram_bot.py
        ``` 
    - **Бот с базой данных:**
       ```bash
       python bd_bot.py
       ```
    - **Добавление метода оплаты:**
       ```bash
       python main_payment_bot.py
       ```

3. Запуск ngrok для туннелирования (для работы с HTML файлом: index.html):
    ```bash
    ngrok http 5000
    ```

## Функции

- **Изменение фотографий:** Используйте команду `/photo` для отправки и изменения фотографий.
- **Ответы на сообщения:** Бот может отвечать на сообщения пользователей.
- **Погода:** Используйте команду `/weather` для получения текущей погоды.
- **Курсы валют:** Используйте команду `/currency` для получения текущих курсов валют.
- **Веб-приложение:** Бот включает функционал полноценного веб-приложения.
- **Оплата:** Интеграция различных способов оплаты.
- **Развертывание на Render:** Инструкции по развертыванию на сервере Render.
- **ngrok:** Используется для туннелирования и тестирования локально развернутого бота.

