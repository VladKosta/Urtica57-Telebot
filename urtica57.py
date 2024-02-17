import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message (message.chat.id, "Привет, {0.first_name}!".format(message.from_user, bot.get_me()))


@bot.message_handler(content_types=["text"])
def first(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
