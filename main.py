import os
import telebot
from groq import Groq

# Tokenlarni shu yerga yozamiz
TELEGRAM_TOKEN = "8736841116:AAGbNllcjiGQApP-qSf5X9bfQ474ezNC0w0"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message.text,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        answer = chat_completion.choices[0].message.content
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {e}")

bot.infinity_polling()
