from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, executor, types
import openai 
import sys

class Reference:
   '''
   A class to store previously response from chatgpt API

   '''
   def __init__(self) -> None:
      self.response =""
load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")

reference = Reference()

TOKEN = os.getenv("TOKEN")

#MODEL NAME
MODEL_NAME = "gpt-3.5-turbo"

#initialise bot and dispatcher
bot = Bot(token=TOKEN)
dp= Dispatcher(bot)

def clear_past():
   """
   A Function to clear the previous conversion and context.
   """
   reference.response = ""


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message) :
    """
    This handler receives messages with
    """
   
    await message.reply("Hi\n I am Tele Bot!\n How can i assist you? \n Sir, this project is totally developed by me ,Rishikesh (id-23AG61R02, iitkgp)")

if __name__ =="__main__": 
    executor.start_polling(dp, skip_updates=True)   



