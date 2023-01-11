import random
from telegram.ext import Updater, CommandHandler

PHOTO_PATH = 'example.png'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This Bot selects a random line that you send. For example, you can send names. Use this format:")
    context.bot.send_message(chat_id=update.effective_chat.id, text="/random\nname_1\nname_2\nname_3\nname_4\nname_5")
    #context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(PHOTO_PATH, 'rb'))
    

def random_name(update, context):
    names = update.message.text.split('\n')
    chosen_name = random.choice(names)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"The chosen name is: {chosen_name}")

def pic(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(PHOTO_PATH, 'rb'))

updater = Updater(token='', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start)) 
updater.dispatcher.add_handler(CommandHandler('random', random_name))
updater.dispatcher.add_handler(CommandHandler('pic', pic))

updater.start_polling()
