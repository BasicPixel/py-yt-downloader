from telegram.ext import *
from pytube import YouTube

API_KEY = '1865860962:AAGVQPRqFgyRIjTN0izbiMdFzrSPtQT7UOI'

def start(update, context):
    # replies to user with 'Hello there, ....'
    update.message.reply_text('Hello there! I download videos from YouTube. What do you want to download?')

def handle_message(update, context):
    # handles messages by creating video object from text, only if it is a youtube link
    text = str(update.message.text)
    try:
        target = YouTube(text)
        # after object is created, download video to downloads folder
        target.streams.get_lowest_resolution().download(r'D:\User\Downloads')
    except:
    # if it is not a link, reply with 'Video could not be found'
        update.message.reply_text('Video could not be found')
    

def main():
    # see documentation for dispatcher + updater explanation
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    # adds handlers for command '/start', and messages sent by user
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

main()