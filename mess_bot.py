from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import datetime

# Mess Menu Dictionary - UPDATED according to the image
menu = {
    "sunday": {
        "breakfast": ["Mix Parantha", "Curd", "Pickle", "Tea"],
        "lunch": ["Aloo Tamatar", "Veg. Tehri", "Green Chutney", "Sirka Onion", "Masala Chach"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Samosa", "Green Chutney", "Tea"],
        "dinner": ["Green Moong Dal", "Mutar Mushroom"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "monday": {
        "breakfast": ["Bread, Jam, Butter", "Aloo peanut poha", "Cornflakes", "Milk", "Tea"],
        "lunch": ["Rajma Raseela", "Lauki Masala"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Veg Marconi", "Tea"],
        "dinner": ["Kadai Paneer", "Black Masoor Dal"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "tuesday": {
        "breakfast": ["Uttapam", "Sambhar", "Coconut chutney", "Bread, Jam, Butter", "Coffee"],
        "lunch": ["Kadhi Pakoda", "Aaloo Jeera", "Fryms"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Bhelpuri", "Tea"],
        "dinner": ["Arhar Dal Takda", "Mix Vegetable", "Gulab Jamun"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "wednesday": {
        "breakfast": ["Aloo Bhaji", "Poori", "Coffee", "Banana"],
        "lunch": ["Arhar Dal", "Kadai Soya"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Bombay Sandwich", "Tea"],
        "dinner": ["Dal Makhani", "Aloo Gajar Matar"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "thursday": {
        "breakfast": ["Lemon Vermicelli", "Sweet Daliya/Masala Oats", "Bread, Jam, Butter", "Tea"],
        "lunch": ["Black Chana Rassa", "Achari Aaloo", "Poori", "Plain Curd"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Mix Sauce Pasta", "Coffee"],
        "dinner": ["Chana Dal Tadka", "Palak Corn", "Rice Kheer"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "friday": {
        "breakfast": ["Idli", "Sambhar", "Coconut Chutney", "Milk", "Tea"],
        "lunch": ["Phindi Choley", "Aloo Matar"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Dal Kachori", "Bhagji", "Tea"],
        "dinner": ["Mix Dal", "Veg Biryani", "Raita"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "saturday": {
        "breakfast": ["Methi Parantha", "Aloo Tamatar", "Tea", "Milk"],
        "lunch": ["Paneer Butter Masala", "Lobiya Dal"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Corn Chana Chat/Biscuit", "Tea"],
        "dinner": ["Dal Lahsuni Tadka", "Saag", "Suji Halwa"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    }
}

# /menu command
def menu_command(update, context):
    keyboard = [
        [InlineKeyboardButton("Sunday", callback_data='sunday')],
        [InlineKeyboardButton("Monday", callback_data='monday')],
        [InlineKeyboardButton("Tuesday", callback_data='tuesday')],
        [InlineKeyboardButton("Wednesday", callback_data='wednesday')],
        [InlineKeyboardButton("Thursday", callback_data='thursday')],
        [InlineKeyboardButton("Friday", callback_data='friday')],
        [InlineKeyboardButton("Saturday", callback_data='saturday')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Select a day to see the menu:', reply_markup=reply_markup)

# Button click handler
def button(update, context):
    query = update.callback_query
    day = query.data
    query.answer()
    day_menu = menu[day]
    text = f"🍽 {day.capitalize()} Menu 🍽\n\n"
    text += f"🌅 Breakfast: {', '.join(day_menu['breakfast'])}\n\n"
    text += f"🍛 Lunch: {', '.join(day_menu['lunch'])}\nCommon: {day_menu['lunchCommon']}\n\n"
    text += f"☕ Evening Snacks: {', '.join(day_menu['snacks'])}\n\n"
    text += f"🌙 Dinner: {', '.join(day_menu['dinner'])}\nCommon: {day_menu['dinnerCommon']}"
    query.edit_message_text(text=text)

# /today command
def today_command(update, context):
    day_index = datetime.datetime.now().weekday()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = days[day_index]

    day_menu = menu[day]
    text = f"🍽 {day.capitalize()} Menu 🍽\n\n"
    text += f"🌅 Breakfast: {', '.join(day_menu['breakfast'])}\n\n"
    text += f"🍛 Lunch: {', '.join(day_menu['lunch'])}\nCommon: {day_menu['lunchCommon']}\n\n"
    text += f"☕ Evening Snacks: {', '.join(day_menu['snacks'])}\n\n"
    text += f"🌙 Dinner: {', '.join(day_menu['dinner'])}\nCommon: {day_menu['dinnerCommon']}"
    update.message.reply_text(text)

# Auto-schedule function
def send_today_menu(context: CallbackContext):
    chat_id = context.job.context
    day_index = datetime.datetime.now().weekday()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = days[day_index]

    day_menu = menu[day]
    text = f"🍽 {day.capitalize()} Menu 🍽\n\n"
    text += f"🌅 Breakfast: {', '.join(day_menu['breakfast'])}\n\n"
    text += f"🍛 Lunch: {', '.join(day_menu['lunch'])}\nCommon: {day_menu['lunchCommon']}\n\n"
    text += f"☕ Evening Snacks: {', '.join(day_menu['snacks'])}\n\n"
    text += f"🌙 Dinner: {', '.join(day_menu['dinner'])}\nCommon: {day_menu['dinnerCommon']}"
    context.bot.send_message(chat_id=chat_id, text=text)

# Command to start daily schedule
def start_schedule(update, context):
    chat_id = update.message.chat_id
    context.job_queue.run_daily(
        send_today_menu,
        time=datetime.time(hour=2, minute=30),
        context=chat_id
    )
    update.message.reply_text("✅ Daily menu schedule set at 8:00 AM!")

# Main function
def main():
    TOKEN = "8511483309:AAFPjaRsndKwEPi-PdjlhoCxeIGJre4rEKc"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("menu", menu_command))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("today", today_command))
    dp.add_handler(CommandHandler("startschedule", start_schedule))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

