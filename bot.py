from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters import Text
from config.config_token import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from generator.generator import *
from generator.selen_man import *
from generator.selen_women import *
import time


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Для парня", "Для девушки"]
    buttons1 = ["эксперемент для нее", "эксперемент для него"]
    keyboard.add(*buttons).add(*buttons1)
    await message.reply("Привет!\n Я бот который будет тебя материть. \n Осталось определится с полом", reply_markup=keyboard)





@dp.message_handler(Text(equals="Для парня"))
async def with_puree(message: types.Message):
    await message.answer(for_man())


@dp.message_handler(Text(equals="Для девушки"))
async def with_puree(message: types.Message):
    await message.answer(for_women())


@dp.message_handler(Text(equals="эксперемент для нее"))
async def with_puree(message: types.Message):
    await message.answer(women())

@dp.message_handler(Text(equals="эксперемент для него"))
async def with_puree(message: types.Message):
    await message.answer(man())


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, timeout=2)
