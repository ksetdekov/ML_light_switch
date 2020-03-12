import telebot
from telebot import apihelper

ip = '94.102.52.30'
port = '1080'

apihelper.proxy = {
    'https': 'socks5h://{}:{}'.format(ip, port)
}
with open("bottoken.txt", "r") as f:
    token = f.readlines()
bot = telebot.TeleBot(token[0])


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
