import telebot

bot = telebot.TeleBot("993023120:AAEm7N8kYw49Bhj7xNBzptSXu_xKn2xodtA")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
