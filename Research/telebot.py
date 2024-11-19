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
MODEL_NAME = "gpt-3.5-turbo-0125"

#initialise bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher= Dispatcher(bot)

def clear_past():
   """
   A Function to clear the previous conversion and context.
   """
   reference.response = ""


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message) :
    """
    This handler receives messages with
    """
   
    await message.reply("Hi\n I am Tele Bot!\n How can i assist you? \n Sir, this project is totally developed by me ,Rishikesh (id-23AG61R02, iitkgp)")


@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
   """
   A handler to clear the previous conversation and context.
   """
   clear_past()
   await message.reply("I have cleared the past conversation and context.")


@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
  """
  A handler to display the help menu.
  """ 
  help_command = """
  Hi,there ,I am chatgpt telegram bot created by Rishikesh,ID-23AG61R02,IIT KGP !Please follow these commands -
  /start - to start the conversation
  /clear- to clear the past converstaion and context.
  /help - to get this help menu.
  I hope this helps,:)
  """
  await message.reply(help_command)


@dispatcher.message_handler()
async def chatgpt(message: types.Message):
   """
   A handler to process the users input and generate the response using the chatgpt API.
   """
   print(f">>> USER:\n\t{message.text}")
   response = openai.ChatCompletion.create(
      model= MODEL_NAME,
      messages = [
         {"role": "assistant", "content": reference.response}, #role assistant
         {"role":"user", "content": message.text} #our query
      ]
   )
   reference.response = response['choices'][0]['message']['content']
   print (f">>> chatgpt: \n\t{reference.response}")
   await bot.send_message(chat_id = message.chat.id , text =reference.response)


if __name__ =="__main__": 
    executor.start_polling(dispatcher, skip_updates=True)   



