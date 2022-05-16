TOKEN = '5342018558:AAGCcnEgNMrtFydVYp-JfLRZNP3Ru99sNGQ'
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

driver.get("https://generator-matov.github.io/")
mat = driver.find_element(By.XPATH, '/html/body/div/div[3]/a[5]').click()
time.sleep(2)
elem = driver.find_element(By.XPATH, '//*[@id="mat"]')

# elem1 = driver.find_element_by_class_name("mat")
print(elem.text)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['mat'])
async def process_help_command(message: types.Message): 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

driver.get("https://generator-matov.github.io/")
mat = driver.find_element(By.XPATH, '/html/body/div/div[3]/a[5]').click()
time.sleep(2)
elem = driver.find_element(By.XPATH, '//*[@id="mat"]')
    await message.reply(elem.text)
    

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
