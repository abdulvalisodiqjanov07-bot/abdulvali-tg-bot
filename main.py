import telebot
from groq import Groq

# Tokenlaringizni qo'shtirnoq ichiga yozing
TELEGRAM_TOKEN = "8736841116:AAGbNllcjiGQApP-qSf5X9bfQ474ezNC0w0"
GROQ_API_KEY = "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
"

# Bot va Groq klentini ishga tushirish
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Groq orqali javob olish (eng barqaror model)
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        answer = chat_completion.choices[0].message.content
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Kechirasiz, xatolik yuz berdi: {e}")

# Botni doimiy ishlab turishi uchun
if __name__ == "__main__":
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.infinity_polling()
