import asyncio
import os

from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from celery_app import send_info
from dispatcher import dp

load_dotenv()


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(f"Salom {message.from_user.first_name}")
    await message.answer(f"Kun.uz dagi eng so'nggi ma'lumot uchun /yangiliklar ni bosing")


data = send_info()


@dp.message(lambda msg: msg.text == '/yangiliklar')
async def send_information(message: Message):
    my_data = data["date"], data["year"], data["info1"], *data["info2"]
    photo = FSInputFile('example-firefox.png', filename='screenshot')
    await message.answer_photo(photo)
    await message.answer(''.join(c for c in str(my_data) if c not in ',()\''))


async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
