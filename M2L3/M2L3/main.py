import telebot
from config import token
from collections import defaultdict
from logic import quiz_questions

user_responses = defaultdict(int)  
points = defaultdict(int)  

bot = telebot.TeleBot(token)

def send_question(chat_id):
    # Отправка вопроса пользователю
    question = quiz_questions[user_responses[chat_id]]
    bot.send_message(chat_id, question.get_text, reply_markup=question.gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    question = quiz_questions[user_responses[chat_id]]
    
    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        points[chat_id] += 1  # Добавляем очки за правильный ответ
    else:
        bot.answer_callback_query(call.id, "Answer is wrong")
    
    user_responses[chat_id] += 1  

    
    if user_responses[chat_id] >= len(quiz_questions):
       
        bot.send_message(chat_id, f"Конец! Ваш счет : {points[chat_id]}/{len(quiz_questions)}")
    else:
        
        send_question(chat_id)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    if chat_id not in user_responses:
        user_responses[chat_id] = 0
        points[chat_id] = 0 
        send_question(chat_id)

bot.infinity_polling()