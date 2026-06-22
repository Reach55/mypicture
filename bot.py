import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Replace with your actual token or load via environment variables
TOKEN = "8850302503:AAE-0Bn30lYzehGKQVlDg_Wzl8xIFglWLnA"
BASE_URL = "https://mypicture-w0w2.onrender.com"  # Your deployment domain

async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.photo:
        return

    # Grab the highest resolution photo available
    photo = update.message.photo[-1]
    file = await photo.get_file()
    
    photo_id = photo.file_unique_id
    chat_id = update.message.chat_id

    os.makedirs("photos", exist_ok=True)
    filename = f"photos/{photo_id}.jpg"

    # Download to disk
    await file.download_to_drive(filename)

    # Build response link appending chat context parameters
    link = f"{BASE_URL}/view/{photo_id}?chat_id={chat_id}"

    await update.message.reply_text(
        f"Your image is available here. Click to open browser and confirm identity:\n{link}"
    )

def main():
    # Build the application using the token
    app = Application.builder().token(TOKEN).build()
    
    # Add handler to catch incoming photos
    app.add_handler(MessageHandler(filters.PHOTO, receive_photo))
    
    print("Bot is listening for photos...")
    
    # Start the polling loop
    app.run_polling()

if __name__ == '__main__':
    main()