from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token='5729459971:AAEocY-4n-2PISfSjKOV2SKR5DloZb2goVY')
dp = Dispatcher(bot=bot)

async def on_startup(_):
    print('Started...')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="/help")
b2 = KeyboardButton(text="/vote")
kb.add(b1, b2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome!',
                           reply_markup=kb)



if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)