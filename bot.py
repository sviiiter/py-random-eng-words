import telebot
from telebot.types import Message

from config import telega_token, telega_chat_id
from extract import extract

bot = telebot.TeleBot(token=telega_token, parse_mode='HTML')


@bot.message_handler(commands=['list'])
def list_words(container_message: Message):
    bot.send_message(chat_id=telega_chat_id, text=str(extract()))


@bot.message_handler(commands=['idf'])
def chat_id(container_message: Message):
    bot.send_message(chat_id=container_message.chat.id, text=str(container_message.chat.id))
