from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


bot = Bot(token='5729459971:AAEocY-4n-2PISfSjKOV2SKR5DloZb2goVY')
dp = Dispatcher(bot=bot)

async def on_startup(_):
    print('Started...')


kb = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text="Ввод перевозчика", callback_data="b1")
b2 = InlineKeyboardButton(text="перевозчика", callback_data="b2")
kb.add(b1, b2)

kb1 = InlineKeyboardMarkup(row_width=2)
b11 = InlineKeyboardButton(text="Ввод 2 перевозчика", callback_data="b11")
b21 = InlineKeyboardButton(text="2 перевозчика", callback_data="b21")
kb1.add(b11, b21)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome!',
                           reply_markup=kb)

@dp.callback_query_handler(lambda call: "b1" in call.data)
async def next_keyboard(call):
    await call.message.edit_reply_markup(kb1)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)