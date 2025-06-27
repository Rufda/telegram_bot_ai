import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardMarkup
import openai
import asyncio

# Load environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if TELEGRAM_BOT_TOKEN is None:
    raise RuntimeError("TELEGRAM_BOT_TOKEN env var is missing")
if OPENAI_API_KEY is None:
    raise RuntimeError("OPENAI_API_KEY env var is missing")

openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

WELCOME_MESSAGE = (
    "Ciao! Sono un bot che usa GPT-3.5-turbo per rispondere ai tuoi messaggi.\n"
    "Scrivimi qualcosa e ti risponder\u00f2!"
)

async def generate_reply(text: str) -> str:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.exception("OpenAI request failed")
        return "Si \u00e8 verificato un errore nel contattare il servizio OpenAI. Riprova pi\u00f9 tardi."

@dp.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(WELCOME_MESSAGE)

@dp.message(F.text)
async def echo(message: Message) -> None:
    reply = await generate_reply(message.text)
    await message.answer(reply)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
