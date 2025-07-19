from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات من آنلاین است ✅")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7710339310:AAHYUgVvbUPkUPYBPSSGGw5pYdIOqcIDr_g").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

