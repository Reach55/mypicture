from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = "8850302503:AAE-0Bn30lYzehGKQVlDg_Wzl8xIFglWLnA"

async def receive_photo(update: Update,
                        context: ContextTypes.DEFAULT_TYPE):

    photo = update.message.photo[-1]
    file = await photo.get_file()

    photo_id = photo.file_unique_id

    os.makedirs("photos", exist_ok=True)

    filename = f"photos/{photo_id}.jpg"
    await file.download_to_drive(filename)

    link = f"https://mypicture-w0w2.onrender.com/view/{photo_id}"

    await update.message.reply_text(
        f"Your page:\n{link}"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.PHOTO, receive_photo)
)

print("Bot running...")
app.run_polling()