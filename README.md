# telegram_AI_bot

**telegram_AI_bot** — это Telegram-бот на Python, использующий OpenAI (или совместимую AI-систему) для генерации ответов на сообщения пользователей в чате.

## Возможности

- Получение сообщений от пользователей Telegram.
- Отправка текста запроса в OpenAI API (или другой совместимый AI-сервис).
- Получение и отправка сгенерированного AI-ответа пользователю.
- Логирование входящих сообщений и ответов.

## Требования

- Python 3.8+
- [aiogram](https://github.com/aiogram/aiogram)
- [openai](https://github.com/openai/openai-python)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- Токен Telegram-бота
- API-ключ и URL для OpenAI-совместимого сервиса

> ⚠️ Точный список зависимостей см. в вашем `requirements.txt`.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/cJlu3/telegram_AI_bot.git
   cd telegram_AI_bot
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте `.env` файл в корне проекта и добавьте переменные:
   ```
   TG_BOT_TOKEN=your_telegram_token
   AI_MODEL=gpt-3.5-turbo
   AI_URL=https://api.openai.com/v1
   AI_API=your_openai_api_key
   ```

## Запуск

```bash
python src/main.py
```

## Как работает бот

- Бот получает входящее сообщение.
- Пересылает текст в AI API.
- Получает текстовый ответ и отправляет его пользователю.
- Ведется лог событий (запросы и ответы).

---

[Репозиторий на GitHub](https://github.com/cJlu3/telegram_AI_bot)
