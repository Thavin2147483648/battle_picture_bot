from config import TELEGRAM_API_KEY
import telebot

bot = telebot.TeleBot(TELEGRAM_API_KEY)


def process_text(text):
    arr = [i.strip() for i in text.split('\n')]
    for ind, i in enumerate(arr):
        if len(i) > 0:
            arr[ind] = '>' + arr[ind]
    return arr


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, '>хрюю уи')


@bot.message_handler(content_types=['text'])
def send_bp(message):
    text = message.text
    bot.send_message(message.from_user.id, '\n'.join(process_text(text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
