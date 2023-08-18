import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6629288685:AAGapVsqbkpZu14fambUZpQZypTydFlD6y0'

# List of SEO tips
SEO_TIPS = [
    "Optimize your website's loading speed for better user experience and SEO rankings.",
    "Create high-quality and engaging content that provides value to your audience.",
    "Use relevant keywords in your content, but avoid keyword stuffing.",
    "Optimize your images by reducing their size and using descriptive file names.",
    "Build high-quality backlinks from authoritative websites in your niche.",
    "Optimize your website's meta titles and descriptions for each page.",
    "Utilize header tags (H1, H2, H3, etc.) to structure your content and improve readability.",
    "Regularly update your website with fresh and relevant content.",
    "Ensure your website is mobile-responsive for better user experience and search rankings.",
    "Monitor your website's analytics to track your SEO performance and make improvements.",
]


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Get a Random SEO Tip", callback_data="tip")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Welcome to the SEO Tips Bot!", reply_markup=reply_markup)


def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == "tip":
        random_tip = random.choice(SEO_TIPS)
        query.answer()
        query.edit_message_text(text=random_tip)
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Click /start to get another tip.")


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
