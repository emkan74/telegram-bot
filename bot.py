from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات من آنلاین است ✅")

if __name__ == "__main__":
    app = ApplicationBuilder().token("توکن_تو").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

