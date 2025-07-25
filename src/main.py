import openai
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values, find_dotenv

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

settings = dotenv_values(find_dotenv(".env"))
TG_BOT_TOKEN = str(settings.get("TG_BOT_TOKEN"))
AI_MODEL = str(settings.get("AI_MODEL"))
AI_URL = settings.get("AI_URL")
AI_API = settings.get("AI_API")

client = openai.OpenAI(
    base_url=AI_URL,
    api_key=AI_API,
)


@dp.message()
async def answer_the_message(message: types.Message):
    try:
        user_prompt = str(message.text)
        logging.info(f"log: {user_prompt=}")

        response = client.chat.completions.create(
            model=AI_MODEL,
            messages=[{"role": "user", "content": user_prompt}],
        )

        answer = str(response.choices[0].message.content)
        logging.info(f"log: bot_answer={answer}")

        await message.answer(answer)
    except Exception as e:
        logging.error(f"Error processing message: {e}", exc_info=True)
        await message.answer(f"Error:\n{e}")


async def main() -> None:
    bot = Bot(token=TG_BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
