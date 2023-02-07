from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from menu_keyboards import categories_keyboard
from typing import Union
bot = Bot(token='5729459971:AAEocY-4n-2PISfSjKOV2SKR5DloZb2goVY')
dp = Dispatcher(bot=bot)

async def on_startup(_):
    await create_db()
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

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await list_categories(message)

async def list_categories(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, types.Message):
        await message.answer("Смотри, что у нас есть", reply_markup=markup)
    
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)

async def list_subcategories(callback: types.CallbackQuery):
    markup = await list_sub

@dp.callback_query_handler(lambda call: call.data)
async def next_keyboard(call):
    if call.data == 'b1':
        await call.message.edit_reply_markup(kb1)
    if call.data == 'b2':
        await call.message.reply("Первая инлайн кнопка", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)