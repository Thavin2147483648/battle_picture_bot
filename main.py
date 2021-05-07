import telebot
from config import TELEGRAM_API_KEY, IMAGE_PATH
from bp_creator import BPCreator

bot = telebot.TeleBot(TELEGRAM_API_KEY)
bp_creator = BPCreator(IMAGE_PATH)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, '>хрюю уи')


@bot.message_handler(content_types=['text'])
def send_bp(message):
    text = bp_creator.process_text(message.text)
    bot.send_message(message.from_user.id, text)
    with open(bp_creator.create_bp(text), 'rb') as img:
        bot.send_photo(message.from_user.id, img)


if __name__ == '__main__':
    bot.polling(none_stop=True)
