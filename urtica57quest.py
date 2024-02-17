import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(
        message.chat.id, "Доброго времени суток, {0.first_name}! 😊 \nРад видеть тебя в моём квесте про третью литературную столицу России😊 .Пожалуйста,пиши ответы на вопросы с большой буквы,иначе ответ не будет принят)\nИтак, к первому вопросу.".format)


def info(message):
    if message.text == ['Информация']:
        bot.send_message(
            message.chat_id, "Я бот,помогающий людям узнать больше про крапивницу в удобной игровой форме) По вопросам улучшения бота пишите:")

    bot.send_message(
        message.chat.id, "Вопрос №1:\nФамилия самого известного писателя родом из Орла?")


text = "Тургенев"
print(text.lower())


@bot.message_handler(content_types=["text"])
def kvest(message):

    if message.text in ("Тургенев", "И.С.Тургенев", "Иван Сергеевич Тургенев", "Тургенев Иван Сергеевич "):
        bot.send_message(message.from_user.id,
                         "Это правильный ответ.\nЯ в тебе не сомневался")
        bot.send_message(message.from_user.id,
                         "Вопрос №2:\nВ каком году был основан город Орел?")
    elif message.text in ("1566", "В 1566 году"):
        bot.send_message(message.from_user.id,
                         "Я верю что ты умн(ый/ая), а не отвечал(а) подбором 😊")
        bot.send_message(
            message.from_user.id, "Вопрос №3:\nСколько лет исполнилось городу Орел в 2016 году?")
    elif message.text in ("450", "450 лет"):
        bot.send_message(
            message.from_user.id, "Правильный ответ.Скажи честно,у тебя были 'пятерки' по математике?)")
        bot.send_message(
            message.from_user.id, "Вопрос №4:\nКак называется узор,представленный на картинке?")
        with open('img/semenova-mariya-orlovskaya-obl_1-1-scaled.jpg', 'rb') as photo1:
            bot.send_photo(message.from_user.id, photo1,
                           caption="<b>Что это за узор?</b>", parse_mode="HTML")
    elif message.text in ("Орловский спис"):
        bot.send_message(
            message.from_user.id, "Вау,это был непростой вопрос!Очень хвалю за проявленную эрудицию)")
        bot.send_message(
            message.from_user.id, "Вопрос №5:\nКак называется сыпь,изображенная на картинке?")
        with open('img/1024px-EMminor2010.jpeg', 'rb') as photo2:
            bot.send_photo(message.from_user.id, photo2,
                           caption="<b>Как называется эта сыпь?</b>")
    elif message.text in ("Волдыри", "Крапивница"):
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('#1')
        btn2 = types.KeyboardButton('#2')
        dunno_btn = types.KeyboardButton('Затрудняюсь ответить')
        markup2.row(btn1, btn2, dunno_btn)
        bot.send_message(message.from_user.id,
                         "Вопрос №6 На какой фотографии изображен Красный мост?")
        with open('img/69_1.JPG', 'rb') as photo3, \
                open('img/Мост_Ока.jpg', 'rb') as photo4:
            bot.send_media_group(
                message.from_user.id, list[photo3, photo4], markup2.row(btn1, btn2, dunno_btn))

    @bot.message_handler(content_types=['text'])
    def func(message):
        if (message.text == '#1'):
            bot.send_message(
                message.chat.id, text="Да,так выглядел Красный мост в начале XX века😊")
        else:
            bot.send_message(
                message.from_user.id, "К сожалению, ответ не правильный.\nПопробуй ещё раз!\nПомни:я принимаю ответы,написанные с большой буквы)")


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
