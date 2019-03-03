import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater('<token>')

def start(bot, update):
    custom_keyboard = [
        ['Бизнес', 'Образование', 'Инфраструктура'],
        ['Коррупция', 'Экология', 'Безопасность']
        ]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id = update.message.chat_id, text = "%s, выберите одну из нижеприведенных категорий:" % update.message.from_user.first_name, reply_markup = reply_markup)

def location(bot, update):
    custom_keyboard = [
        ['г. Алматы', 'г. Астана', 'г. Шымкент'],
        ['г. Атырау', 'г. Павлодар', 'г. Актау']
        ]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(chat_id = update.message.chat_id, text = "Теперь, выберите одну из нижеперечисленных локаций:", reply_markup = reply_markup)

def echo(bot, update):
    if "hello" in update.message.text.lower():
        wtext = "Здравствуйте, %s, этот бот готов к работе, пожалуйста введите команду '/start' " % update.message.from_user.first_name
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "hi" in update.message.text.lower():
        wtext = "Здравствуйте, %s, этот бот готов к работе, пожалуйста введите команду '/start' " % update.message.from_user.first_name
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
    
    elif "привет" in update.message.text.lower():
        wtext = "Здравствуйте, %s, этот бот готов к работе, пожалуйста введите команду '/start' " % update.message.from_user.first_name
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "здравствуйте"in update.message.text.lower():
        wtext = "Здравствуйте, %s, этот бот готов к работе, пожалуйста введите команду '/start' " % update.message.from_user.first_name
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "Бизнес" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "Образование" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "Инфраструктура" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
    
    elif "Коррупция" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "Экология" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "Безопасность" in update.message.text:
        wtext = "Отлично, сейчас пропешите команду '/location' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "г. Алматы" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "г. Астана" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "г. Шымкент'" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
    
    elif "г. Атырау" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "г. Павлодар" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

    elif "г. Актау" in update.message.text:
        wtext = "Большое спасибо, ваш ответ записан."
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)
     
    else:
        wtext = "Ой, как некультурно не здароваться, введите команду '/start' "
        bot.sendMessage(chat_id = update.message.chat_id, text = wtext)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('location', location))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
