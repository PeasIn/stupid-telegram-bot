from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler


key_token = "6977851314:AAEb6SpkOWJDTqZjiTcNc4v3gieXvu_SSx4" #Masukkan KEY-TOKEN BOT 
user_bot = "@legeratelbot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("use /help for list of chats")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("prompt: halo, selamat pagi, selamat siang, selamat sore, selamat mala, siapa kamu, apa musik favorit")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima:
        await update.message.reply_text("Hallo juga")
    elif 'selamat pagi' in text_lwe_diterima:
        await update.message.reply_text("pagi")
    elif 'selamat siang' in text_lwe_diterima:
        await update.message.reply_text("siang")
    elif 'selamat sore' in text_lwe_diterima:
        await update.message.reply_text("sore")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("malam")
    elif 'apa musik favorit' in text_lwe_diterima:
        await update.message.reply_text("Heaven Can Wait by mikael jekson")
    elif 'siapa kamu' in text_lwr_diterima:
        await update.message.reply_text(f"beep bop im a bot : {user_bot}")
    else:
        await update.message.reply_text("?")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("gambar kamu jelek")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"err {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)