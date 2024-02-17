import random
from telegram import ReplyKeyboardMarkup

questions = {"Как звали царя,при котором был основан город Орел?", "В каком году был основан город Орел?", "Главный элемент сыпи при крапивнице?"}
correct_answers = {"Иван IV Грозный", "1566", "волдырь"}
wrong_answers = [{"Петька", "988", "пятно"}, {"Петр I Великий", "1704", "узелок"}, {"Борис Годунов", "1146", "эрозия"}]

def quiz(update, context):
    random_question = random.sample(questions, 1)
    correct_answer = list(correct_answers)[list(questions).index(random_question)]
    keyboard = [[i] for i in wrong_answers[random.randint(0,2)]] + [[correct_answer]]
    random.shuffle(keyboard)
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вопрос: {}\n".format(random_question[0]), reply_markup=reply_markup)