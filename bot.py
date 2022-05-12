TOKEN = '5342018558:AAGCcnEgNMrtFydVYp-JfLRZNP3Ru99sNGQ'
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
# from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


list_mat = ['говно', 'писька', 'жопа', "пидр", "урод"]
# test = random.choice(list_mat)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['mat'])
async def process_help_command(message: types.Message):    
    await message.reply(text = random.choice(list_mat))
    

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)