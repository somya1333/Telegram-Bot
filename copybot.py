import logging
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update,ReplyKeyboardMarkup
from util import get_reply,fetch_news,topics_keyboard
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

TOKEN="Put your Bot token here"

app=Flask(__name__)
@app.route(f"/{TOKEN}",methods=["GET",'POST'])
def webhook():
    #webhook view which receives updates from telegram
    # create update object from json-format request data
    update=Update.de_json(request.get_json(),bot)
    #process update
    dp.process_update(update)
    return "ok" 
def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply=f"Hi! {author}"
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def _help(bot,update):
    author=update.message.from_user.first_name
    help_txt= f"I will help you {author}"
    bot.send_message(chat_id=update.message.chat_id,text=help_txt)
def reply_text(bot,update):
    intent,reply=get_reply(update.message.text,update.message.chat_id)
    if intent=='get_news':
        articles=fetch_news(reply)
        for  article in articles:
            bot.send_message(chat_id=update.message.chat_id,text=article['link'])
    else:
        bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
def news(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="Choose a category",
    reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard,one_time_keyboard=True))
def error(bot,update):
    logger.error(f"Update {update} caused error {update.error}")
if __name__ == "__main__":
    bot=Bot(TOKEN)
    bot.set_webhook("Put the ngrok https url link here"+TOKEN)
    dp=Dispatcher(bot,None)
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(CommandHandler("news",news))
    dp.add_handler(MessageHandler(Filters.text,reply_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)