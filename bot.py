from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor

from config.config_token import TOKEN
from config.config_token import WETHER_TOKEN
from generator.generator import *
from wether.wether import open_wether

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class Form(StatesGroup):
    city = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Для парня", "Для девушки"]
    buttons1 = ["узнать погоду"]
    # buttons1 = ["эксперемент для нее", "эксперемент для него"] .add(*buttons1)
    keyboard.add(*buttons).add(*buttons1)
    await message.reply("Привет!\n Я бот который будет тебя материть. \n Осталось определится с полом",
                        reply_markup=keyboard)


@dp.message_handler(Text(equals="Для парня"))
async def with_puree(message: types.Message):
    await message.answer(for_man())


@dp.message_handler(Text(equals="Для девушки"))
async def with_puree(message: types.Message):
    await message.answer(for_women())


@dp.message_handler(Text(equals="узнать погоду"))
async def wether_time(message: types.Message):
    await Form.city.set()
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")


@dp.message_handler(state=Form.city)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        city = data['city']
        res = open_wether(city, WETHER_TOKEN)
        await message.answer(res)
        # await bot.send_video(message.chat.id, 'https://i.gifer.com/8YCn.gif', None)
    await state.finish()


# @dp.message_handler(Text(equals="эксперемент для нее"))
# async def with_puree(message: types.Message):
#     await message.answer(women())
#
# @dp.message_handler(Text(equals="эксперемент для него"))
# async def with_puree(message: types.Message):
#     await message.answer(man())


@dp.message_handler()
async def echo_message(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, timeout=2)
