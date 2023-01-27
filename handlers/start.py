from aiogram import types, Dispatcher
from create import dp, bot

# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")

# @dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(echo_message)