from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Mess Menu Dictionary
menu = {
    "sunday": {
        "breakfast": ["Mix Parantha", "Curd", "Pickle", "Tea"],
        "lunch": ["Aloo Chole", "Masala Poori", "Green Chutney", "Sirka Onion", "Lassi"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Samosa", "Green Chutney", "Tea"],
        "dinner": ["Black Mascot Dal", "Matar Mushroom"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "monday": {
        "breakfast": ["Bread, Jam, Butter", "Aloo peanut poha", "Cornflakes", "Milk", "Tea"],
        "lunch": ["Rajma Raseela", "Lauki Masala"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Coleslaw Sandwich", "Tea"],
        "dinner": ["Cheese Chilli Gravy", "Fried Rice", "Moong Mascor Dal"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "tuesday": {
        "breakfast": ["Uttapam", "Sambhar", "Coconut chutney", "Bread, Jam, Butter", "Coffee"],
        "lunch": ["Kadhi Pakoda", "Aaloo Jeera", "Fryms"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Corn Chana Chat", "Manchow Soup"],
        "dinner": ["Arhar Dal Takda", "Mix Vegetable", "Gulab Tanum"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "wednesday": {
        "breakfast": ["Aloo Bhaji", "Poori", "Coffee", "Banana"],
        "lunch": ["Arhar Dal", "Aloo Soya"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Bread Pakoda", "Green Chutney", "Tea"],
        "dinner": ["Urdh Rajma", "Aloo Gobbi", "Rice Kneer"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "thursday": {
        "breakfast": ["Lemon Vermicelli", "Sweet Daliya", "Bread, Jam, Butter", "Tea"],
        "lunch": ["Black Chana Rassa", "Achari Aaloo", "Poori", "Plain Curd"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Mix Sauce Pasta", "Coffee"],
        "dinner": ["Dal Harvall", "Aloo Gajar Matar"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "friday": {
        "breakfast": ["Idli", "Sambhar", "Coconut Chutney", "Milk", "Tea"],
        "lunch": ["Phindi Choley", "Kadai Soya"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Dal kachori", "Bhagji", "Tea"],
        "dinner": ["Mix Dal", "Veg Rhyani", "Raita"],
        "dinnerCommon": "Rice, Pickle, Chapati, Salad"
    },
    "saturday": {
        "breakfast": ["Methi Parantha", "Aloo Tamatar", "Tea", "Milk"],
        "lunch": ["Paner Butter Masala", "Moong Dal Takda"],
        "lunchCommon": "Rice, Pickle, Chapati, Salad & Curd",
        "snacks": ["Mix Pakoda", "Saunth", "Tea"],
        "dinner": ["Dal Lehsumi Tadka", "Saag", "Fruit Custard"],
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
    text += f"☕ Snacks: {', '.join(day_menu['snacks'])}\n\n"
    text += f"🌙 Dinner: {', '.join(day_menu['dinner'])}\nCommon: {day_menu['dinnerCommon']}"
    query.edit_message_text(text=text)

# Main function
def main():
    updater = Updater("8511483309:AAFPjaRsndKwEPi-PdjlhoCxeIGJre4rEKc", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("menu", menu_command))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()