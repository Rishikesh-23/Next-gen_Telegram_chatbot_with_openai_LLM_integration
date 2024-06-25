import logging
from aiogram import Bot, Dispatcher, executor, types


from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
#print()

#configure logging
logging.basicConfig(level=logging.INFO)

#initialise bot and dispatcher
bot = Bot(token=API_TOKEN)
dp= Dispatcher(bot)

@dp.message_handler(commands=['start','help'])

async def command_start_handler(message: types.Message) :
    """
    This handler receives messages with `/start` command
    """
   
    await message.reply("Hi\n I am echo Bot!\n Powered by aiogram.\n \n Sir, this project is totally developed by me ,Rishikesh (id-23AG61R02, iitkgp)")

@dp.message_handler(commands=['start','help'])
async def echo(message: types.Message) :
    """
    This willreturn echo
    """
   
    await message.answer(message.text)


if __name__ =="__main__": 
    executor.start_polling(dp, skip_updates=True)   