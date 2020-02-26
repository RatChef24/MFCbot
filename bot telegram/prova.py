import telebot
import time
import os

botToken='1070241227:AAGNN87DedcRq3vC7edg42fHbltf8fzNNMA'

bot= telebot.TeleBot(token=botToken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Fottiti')



@bot.message_handler(func=lambda message:message.text=='Ciao' and message.chat.username=='El_ricki')
def echo_all(message):
	bot.reply_to(message, 'Salve sommo Padrone, come la posso servire?')

@bot.message_handler(func=lambda message: message.text == "ciao" or message.text=='Ciao')
def command_text_hi(message):
    #bot.send_message(message.chat.id,'fanculo')
    bot.reply_to(message, 'fancul a mammt')


@bot.message_handler(func=lambda message:message.chat.type=='supergroup')
def testPrivate(message):
    bot.send_message(message.chat.id, 'bestia')

#@bot.message_handler(func=lambda message:message.chat.type=='supergroup')
#def testPrivate(message):
#    bot.send_message(message.chat.id, 'minchia')


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.send_message(message.chat.id, 'dab')
    photo=open('test.jpg','rb')
    bot.send_photo(message.chat.id, photo)



bot.polling()
