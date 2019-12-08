from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters


TG_TOKEN = "934760593:AAEYRMAXLlZ3QBV7j4nqfWEMvigVWv5Blpk"

def igive(image, texte):
    igive.image = image
    igive.texte = texte

def message_handler(bot: Bot, update: Update):

    text = update.effective_message.text
    reply_text = "Bot funguje, odpoved: " + str(text)

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text)



def main():
    bot = Bot(
        token=TG_TOKEN
    )
    updater= Updater(
        bot=bot
    )

    image = False
    texte = False
    igive(image, texte)

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
