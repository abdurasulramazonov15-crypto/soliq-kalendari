
import os
import logging

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.environ["BOT_TOKEN"]

APP_URL = "https://abdurasulramazonov15-crypto.github.io/soliq-kalendari/"

logging.basicConfig(level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📅 Soliq taqvimini ochish",
                web_app=WebAppInfo(url=APP_URL),
            )
        ]
    ]

    text = (
        "🇺🇿 Assalomu alaykum!\n\n"
        "Sizni Soliq Taqvimi botida ko‘rib turganimizdan mamnunmiz!\n\n"
        "📅 Soliq hisobotlari va muhim sanalarni kuzating.\n"
        "🧮 Soliq kalkulyatoridan foydalaning.\n"
        "📌 Soliq majburiyatlaringizni qulay boshqaring.\n\n"
        "Quyidagi tugmani bosib, soliq taqvimini oching!"
    )

    await update.effective_message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def app_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "ℹ️ Botdan foydalanish:\n\n"
        "/start — botni ishga tushirish\n"
        "/app — soliq taqvimini ochish\n"
        "/help — yordam\n\n"
        "Soliq taqvimini ochish uchun /app buyrug‘ini yuboring."
    )


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app_command))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()


if __name__ == "__main__":
    main()
