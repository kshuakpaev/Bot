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

@dp.callback_query_handler(lambda call: call.data)
async def next_keyboard(call):
    if call.data == 'b1':
        await call.message.edit_reply_markup(kb1)
    if call.data == 'b2':
        await call.message.reply("Первая инлайн кнопка", reply_markup=kb)


@dp.message_handler(commands=["random"])
async def process_random(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("Рандомное число", callback_data="btnRandom"))
    # markup.add(InlineKeyboardButton(league, callback_data=f"prefix:{league_cd}"))
    await message.answer("Пожалуйста, выберите из списка:", reply_markup=markup)


# зачем тебе text_startswith? У тебя же четкий btnRandom, а не какой-то так btnRandom:123
@dp.callback_query_handler(text_startswith="btnRandom")
async def random_button(callback: types.CallbackQuery):
    await callback.answer()
    # зачем это условие? для кого оно? Если хендлер сработал значит дата и будет равана этому значению
    # data = callback.data
    # if data == "btnRandom":
    # а это что за бесмысленная функция? Убери ее
    # async def randomizer(message: types.Message):
    #     random_markup = InlineKeyboardMarkup(row_width=1).add(
    #         InlineKeyboardButton(text="Вы выбрали рандом", callback_data="Random"))
    #     await callback.message.answer("Рандомное меню:", reply_markup=random_markup)
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Вы выбрали рандом", callback_data="Random"))
    await callback.message.answer("Рандомное меню:", reply_markup=markup)


# и не запихивай хендлер внурь другого хендлера НИКОГДА
@dp.callback_query_handler(text="Random")
async def random_selected(callback: types.CallbackQuery):
    await callback.answer()
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Вы выбрали рандом", callback_data="Random"))
    await callback.message.answer("Вы выбрали рандомное число", reply_markup=markup)        

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)