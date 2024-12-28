import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Геттер для получения текста вопроса
    @property
    def get_text(self):
        return self.__text

    # Метод для генерации Inline клавиатуры
    def gen_markup(self):
        markup = InlineKeyboardMarkup()
        for i, option in enumerate(self.options):
            callback_data = 'correct' if i == self.__answer_id else 'wrong'
            markup.add(InlineKeyboardButton(option, callback_data=callback_data))
        return markup

# Вопросы
quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент", "101 способ уснуть", "Пособие по управлению людьми"),
    Question("Кто проживает на дне океана?", 0, "Губка-боб", "Патрик", "Мистер Крабс", "Ёжик"),
    Question("Что программисты говорят, когда код работает, но не совсем так, как ожидается?", 1, "Просто нужно немного подождать", "Это не баг, это фича!", "Я это специально сделал так"),
    Question("Что программист делает после того, как исправил баг?", 2, "Пишет отчёт о том, как всё было сложно", "Идёт на обед", "Проверяет, не появился ли новый"),
    Question("Как программисты называют процесс тестирования?", 2, "Проверка", "Гадание на кофейной гуще", "Необходимая рутина")
]
