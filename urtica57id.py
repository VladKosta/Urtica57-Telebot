import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=["photo"])

def handle_photo(message):
    photo_id=message.photo[3].file_id
    file_info = bot.get_file(photo_id)
    print(photo_id) # Выводим file_id
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')
    bot.send_message(message.chat.id, photo_id)


bot.polling(none_stop=True)

