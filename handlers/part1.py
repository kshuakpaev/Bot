from aiogram import types, Dispatcher
from create import dp

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('Помоги себе сам!')

def register_handlers_part1(dp: Dispatcher):
    dp.register_message_handler(process_help_command, commands=['help'])