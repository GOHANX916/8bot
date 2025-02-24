import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7808256697:AAH3L97_dgi8uins4yeXLtef_xyZ5mQxAIU"  # Replace with your bot token
USERS_FILE = "users.json"

# Load users from file
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

# Main menu keyboard
main_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("📘 FACEBOOK ID"), KeyboardButton("🌍 GOOGLE ID")],
    [KeyboardButton("❓ HOW TO USE"), KeyboardButton("🔄 UPDATE BOT")],
    [KeyboardButton("💰 MY BALANCE"), KeyboardButton("📦 STOCK")],
    [KeyboardButton("☎️ CONTACT")]
], resize_keyboard=True)

# Facebook ID purchase keyboard
facebook_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("F-BUY 1"), KeyboardButton("F-BUY 2"), KeyboardButton("F-BUY 3")],
    [KeyboardButton("F-BUY 4"), KeyboardButton("F-BUY 5"), KeyboardButton("F-BUY 6")],
    [KeyboardButton("F-BUY 7"), KeyboardButton("F-BUY 8"), KeyboardButton("F-BUY 9")],
    [KeyboardButton("F-BUY 10"), KeyboardButton("F-BUY 11"), KeyboardButton("F-BUY 12")],
    [KeyboardButton("🚪 Exit")]
], resize_keyboard=True)

# Google ID purchase keyboard
google_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("G-BUY 1"), KeyboardButton("G-BUY 2"), KeyboardButton("G-BUY 3")],
    [KeyboardButton("G-BUY 4"), KeyboardButton("G-BUY 5"), KeyboardButton("G-BUY 6")],
    [KeyboardButton("G-BUY 7"), KeyboardButton("G-BUY 8"), KeyboardButton("G-BUY 9")],
    [KeyboardButton("G-BUY 10"), KeyboardButton("G-BUY 11"), KeyboardButton("G-BUY 12")],
    [KeyboardButton("🚪 Exit")]
], resize_keyboard=True)

# /start command handler
async def start(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    users = load_users()

    if user_id not in users:
        users.append(user_id)
        save_users(users)

    await update.message.reply_text(
        f"❤️HEY @{update.message.from_user.username}\n\n"
        "🔥WELCOME TO 8 LEVEL ID SELLER BOT\n\n"
        "☎️ ANY PROBLEM? CONTACT \n"
        "@Gohan52",
        reply_to_message_id=update.message.message_id,
        reply_markup=main_keyboard
    )

# Handle user button clicks
async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "📘 FACEBOOK ID":
        await update.message.reply_text("Select a FACEBOOK ID to buy:", reply_markup=facebook_keyboard)
    elif text == "🌍 GOOGLE ID":
        await update.message.reply_text("Select a GOOGLE ID to buy:", reply_markup=google_keyboard)
    elif text == "🚪 Exit":
        await update.message.reply_text("Returning to the main menu.", reply_markup=main_keyboard)
    elif text.startswith("F-BUY"):
        await update.message.reply_text(f"You selected {text}. Processing your request...")
    elif text.startswith("G-BUY"):
        await update.message.reply_text(f"You selected {text}. Processing your request...")
    else:
        responses = {
            "❓ HOW TO USE": "Here's how to use the bot! 🤖",
            "🔄 UPDATE BOT": "Bot update coming soon! 🔄",
            "💰 MY BALANCE": "Your current balance is: ₹0 💰",
            "📦 STOCK": "📦 Checking stock availability...",
            "☎️ CONTACT": "☎️ Contact support at @Gohan52"
        }
        if text in responses:
            await update.message.reply_text(responses[text])

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
