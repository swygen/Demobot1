from telegram.ext import Updater, CommandHandler

TOKEN = "8139445667:AAE09RTC7M2b1NDU4ffPY0BRAmYyJJTxgZw"

def start(update, context):
    message = (
        "welcome to Swygen বট।\n"
        "এটা একটা Demo Bot | টেস্টিং এর জন্য তৈরি করা হয়েছে powered by Swygen"
    )
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
