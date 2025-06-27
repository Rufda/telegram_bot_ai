import asyncio
import logging
import os

import openai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


logging.basicConfig(level=logging.INFO)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set")

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Ciao! Sono un bot AI. Inviami un messaggio e ti risponder\u00f2."
    )


@dp.message()
async def echo_with_gpt(message: types.Message):
    openai.api_key = OPENAI_API_KEY
    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}],
        )
        answer = resp.choices[0].message.content.strip()
    except Exception as e:
        logging.exception("OpenAI API error")
        answer = "Si \u00e8 verificato un errore nel generare la risposta."

    await message.answer(answer)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
