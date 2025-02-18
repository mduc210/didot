import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

async def like(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        uid = context.args[0]
        url = f"https://freefire-virusteam.vercel.app/likes?key=23092003&uid={uid}"
        
        try:
            response = requests.get(url)
            data = response.json()

            if 'message' in data:
                await update.message.reply_text(data['message'])
            
            else:
                await update.message.reply_text("Không có thông tin phản hồi từ API.")
            
        except Exception as e:
            await update.message.reply_text("Có lỗi xảy ra khi gọi API.")
            logger.error(f"Error: {e}")
    else:
        await update.message.reply_text("Vui lòng nhập UID sau lệnh /like.")

def main() -> None:
    # Thay 'apy' bằng token của bot 
    application = ApplicationBuilder().token("apy").build()

    application.add_handler(CommandHandler("like", like))

    application.run_polling()

if __name__ == '__main__':
    main()
