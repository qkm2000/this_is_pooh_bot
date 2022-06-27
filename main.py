import os
import telebot
import yfinance as yf

API_Key = os.environ['API_Key']
bot = telebot.TeleBot(API_Key)

@bot.message_handler(commands = ["start"])
def start(message):
	bot.send_message(message.chat.id,"""Here's the list of all available commands...
					 1. /greet
					 2. /hello
					 3. /iloveyou""")

@bot.message_handler(commands = ["greet"])
def greet(message):
	bot.reply_to(message, "hey bb! i love you :P")

@bot.message_handler(commands = ["hello"])
def hello(message):
	bot.send_message(message.chat.id, "hi! this is your bb speaking!")

@bot.message_handler(commands = ["iloveyou"])
def iloveyou(message):
	bot.reply_to(message, "aww... i love you too :x")

bot.polling()