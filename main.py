# from requests import *
# from telegram import *
# from telegram.ext import *
import telebot
TOKEN = "6606403897:AAEW3pxmb3fhWPv9Vk5rxONDsyPlsAeD-D8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.reply_to(message, start)



RANDOM_IMAGE = "Random image"
GET_MP3 = "Get mp3"
RANDOM_IMG_URL = "https://picsum.photos/1200"

# # Declare IMAGE_COUNTER as a global variable
# global IMAGE_COUNTER
IMAGE_COUNTER = 0


print("Running up the bot...")

# # This command is used to register the commands
# # that the bot will be able to recognize and execute.
# # use_context=True is used to tell the bot to use the new context based callbacks
# # instead of the old deprecated ones.


def start():
    # SENDING HELLO MESSAGE
     reply_text(message, reply_markup=None, **kwargs)
     update.message.reply_text("Hello there! I'm bot. Nice to see you!")
    # ###################################################################
    # SENDING PHOTO
    _send_local_file()


def _send_local_file():
    """
        We must open the file in binary mode, 
        otherwise Telegram will not be able to process it correctly
        ------------------------------------------------------------
        RU: Мы должны открыть файл в двоичном режиме,
        иначе Telegram не сможет обработать его правильно
    """
    with open("images.jfif", "rb") as f:
        """
                update.message.reply_photo(photo, caption=None)
            photo   - Photo to send
            caption - Photo caption, 0-1024 characters
        """
        bot.reply_photo(f, caption="Hello!Nice to meet you!")


 def _send_mp3(update: Update, context: CallbackContext):
     with open("phonk_mood_-_BRAZILIAN_PHONK_FUNK_REMIX_0to8_DJ_Ritmo55_-_Bate_Forte_e_Dana_75518415.mp3", "rb") as f:
         update.message.reply_audio(f, caption="This is mp3")


 def get_attached_buttons(update: Update, context: CallbackContext):
#     """
#         There are some types of buttons
#             1. KeyboardButton  => is used to create a simple button that is displayed below the message
#             2. ReplyKeyboardMarkup => is used to create a custom keyboard with buttons
#                 ---
#                 We use message handler function to handle buttons below message (see: message_handler_for_below_buttons)
#             ----------------
#             3. InlineKeyboardButton => is used to create a button that is attached to the message
#             4. InlineKeyboardMarkup => is used to create a custom keyboard with buttons that are attached to the message
#                 ---
#                 We use callback query handler function to handle buttons attached to the message
#                 (see: callback_query_handler_for_attached_buttons)
#     """

    buttons = [
        [InlineKeyboardButton("Button 1", callback_data="1")],
        [InlineKeyboardButton("Button 2", callback_data="2")]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose option:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


 def get_buttons_below_message(update: Update, context: CallbackContext):
#     """
#         There are some types of buttons
#             1. KeyboardButton  => is used to create a simple button that is displayed below the message
#             2. ReplyKeyboardMarkup => is used to create a custom keyboard with buttons
#                 ---
#                 We use message handler function to handle buttons below message (see: message_handler_for_below_buttons)
#             ----------------
#             3. InlineKeyboardButton => is used to create a button that is attached to the message
#             4. InlineKeyboardMarkup => is used to create a custom keyboard with buttons that are attached to the message
#                 ---
#                 We use callback query handler function to handle buttons attached to the message
#                 (see: callback_query_handler_for_attached_buttons)
#     """

     buttons = [
         [KeyboardButton(RANDOM_IMAGE)],
         [KeyboardButton(GET_MP3)]
     ]
     context.bot.send_message(
         chat_id=update.effective_chat.id,
         text="Choose option:",
         reply_markup=ReplyKeyboardMarkup(buttons)
     )

    

 def callback_query_handler_for_attached_buttons(update: Update, context: CallbackContext):
     query = update.callback_query
     query.answer()
     if query.data == "1":
         query.edit_message_text(text="You pressed button 1")
     elif query.data == "2":
         query.edit_message_text(text="You pressed button 2")


 def message_handler_for_below_buttons(update: Update, context: CallbackContext):
     # Use the global keyword to modify IMAGE_COUNTER
     global IMAGE_COUNTER
     IMAGE_COUNTER += 1
     if update.message.text == RANDOM_IMAGE:
         image = get(RANDOM_IMG_URL).content
         context.bot.sendMediaGroup(
             chat_id=update.effective_chat.id,
             media=[InputMediaPhoto(image, caption=f"Random {IMAGE_COUNTER}")]
         )
     elif update.message.text == GET_MP3:
         _send_mp3(update, context)


 def help(update, context):
     update.message.reply_text("""
 /start   - Start the bot
 /help    - Help
 /buttons_below    - Get Optional buttons
 /buttons_attached - Get Attached buttons
 """
                               )


 updater = Updater(TOKEN, use_context=True)
 dispatcher = updater.dispatcher
 dispatcher.add_handler(CommandHandler("start", start))
 dispatcher.add_handler(CommandHandler("help", help))
 dispatcher.add_handler(CommandHandler('buttons_below', get_buttons_below_message))
 dispatcher.add_handler(CommandHandler('buttons_attached', get_attached_buttons))
 dispatcher.add_handler(MessageHandler(Filters.text, message_handler_for_below_buttons))
 dispatcher.add_handler(CallbackQueryHandler(callback_query_handler_for_attached_buttons))


 updater.start_polling()
 updater.idle()
bot.polling()
