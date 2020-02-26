import telebot
from flask import Flask, request
import os

botToken='1070241227:AAGNN87DedcRq3vC7edg42fHbltf8fzNNMA'
bot= telebot.TeleBot(token=botToken)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Fottiti')



@bot.message_handler(func=lambda message:message.text=='Ciao' and message.from_user.username=='El_ricki')
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
    #photo=open('test.jpg','rb')
    #bot.send_photo(message.chat.id, photo)






@server.route('/' + botToken, methods=['PORT'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://blooming-badlands-17750.herokuapp.com/' + botToken)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
