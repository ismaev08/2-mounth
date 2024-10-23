from aiogram import Bot, Dispatcher
from aiogram.utils import executor

TOKEN = '7099700134:AAGeQBBPn6FxT5b8FTXnmkK6K3-Yl5X6rbY'
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)















if __name__ == 'main':
    executor.start_polling(dp, skip_updates=True)