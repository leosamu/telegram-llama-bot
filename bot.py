import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from llama_index import StorageContext, load_index_from_storage
load_dotenv()
# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define the welcome message
WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE")

# Define the function to handle the /start command
async def  start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_MESSAGE)

# Define the function to handle messages
async def answer(update: Update, context: CallbackContext) -> None:    
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    # load index
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    # generate an answer to the message using our index
    response = query_engine.query(update.message.text)
    # send the answer to the same chat where the bot received the message   
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Define the main function
def main() -> None:
    """Run the bot."""    
    # Set Telegram bot
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_API_KEY")).build()
    
    # /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # we can answer to more commands use the start handler as template if needed
    
    # Message handler this will get all messages that dont have commands and answer them using llama index gpt
    generate_response_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    application.add_handler(generate_response_handler)    
    
    

    # Start bot
    application.run_polling()

if __name__ == '__main__':
    main()
