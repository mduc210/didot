import telebot
import requests
import json

# Thay token bot vào đây
TOKEN = "NHẬP_TOKEN_BOT_VÀO_ĐÂY"
API = "https://freefire-virusteam.vercel.app/likes"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "🔥 Bot buff like Free Fire đã sẵn sàng!\nDùng lệnh: /like <uid> để buff like.")

@bot.message_handler(commands=["like"])
def like_user(message):
    try:
        args = message.text.split()

        if len(args) < 2:
            bot.reply_to(message, "⚠️ Sai cú pháp!\n👉 Dùng: /like <uid>")
            return

        uid = args[1]

        params = {"key": "23092003", "uid": uid}
        response = requests.get(API, params=params)

        if response.status_code == 200:
            data = response.json()
            message_text = data.get("message", "Không có phản hồi từ API.")
            bot.reply_to(message, f"✅ Đã like UID {uid}!\n📩 Phản hồi: {message_text}")
        else:
            bot.reply_to(message, f"❌ Lỗi khi like UID {uid}: {response.text}")

    except json.JSONDecodeError:
        bot.reply_to(message, "❌ API không trả về JSON hợp lệ!")
    except Exception as e:
        bot.reply_to(message, f"❌ Lỗi: {str(e)}")

print("🚀 Bot đang chạy...")
bot.polling()
