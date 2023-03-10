from aiogram import types, Dispatcher
from create import dp, bot
import handlers.murkups as nav
from handlers.murkups import mark_blank_vid

import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from handlers.bdd import BD1
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class Form1(StatesGroup):
    binn = State() 
    nameper = State() 
    gosnum = State() 

# @dp.message_handler(commands=['start1'])
# async def start1(message: types.Message):
#     if message.chat.type == "private":
#         await bot.send_message(message.from_user.id, "Главное меню", reply_markup=nav.mainMenu)
@dp.callback_query_handler(lambda callback: callback.data)
async def next_keyboard(callback):
    print(callback)
    if callback.data == 'btnOutBlank':
        # await callback.message.edit_reply_markup(nav.mainMenu)
        await callback.message.reply("Последовательно введите БИН/ИИН, страну, вид и количество бланков", reply_markup=nav.menuInBlank)
    if callback.data == 'btnOutGruz':
        await callback.message.reply("Первая инлайн кнопка")
    if callback.data == 'btnInBlank':
        # await callback.message.delete() #_message(callback.from_user.id, callback.message.message_id)
        # await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        await callback.message.reply("Последовательно введите БИН/ИИН, страну, вид и количество бланков", reply_markup=nav.menuInBlank)     
    # if callback.data == 'btnInBlank':
        # # @dp.callback_query_handler(text="btnInBlank")
        # async def btn_action(message: types.Message):
        #     await bot.delete_message(message.from_user.id, message.message.message_id)
        #     await bot.send_message(message.from_user.id, "Последовательно введите БИН/ИИН, страну, вид и количество бланков", reply_markup=nav.menuInBlank)
        # pass
    if callback.data == 'btnVInBlank':
        # await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
        await Form1.binn.set()
        await callback.message.reply("Введите БИН/ИИН")
    if callback.data == 

        
# @dp.callback_query_handler(text="btnInBlank")
# async def btn_action(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     await bot.send_message(message.from_user.id, "Последовательно введите БИН/ИИН, страну, вид и количество бланков", reply_markup=nav.menuInBlank)

@dp.callback_query_handler(text="btnMainMenu")
async def btn_action(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Главное меню", reply_markup=nav.mainMenu)

# @dp.callback_query_handler(text="btnVInBlank")
# async def cmd_start(message: types.Message):
#     await bot.delete_message(message.from_user.id, message.message.message_id)
#     await Form1.binn.set()
#     await bot.send_message(message.from_user.id, "Введите БИН/ИИН")
#     # await message.reply("Введите БИН/ИИН")


# # Добавляем возможность отмены, если пользователь передумал заполнять
# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return

#     await state.finish()
#     await message.reply('Отменено пользователем')
#     await bot.send_message(message.from_user.id, "Разместить бланк разрешения", reply_markup=nav.menuInBlank)


# # Сюда приходит ответ с именем
@dp.message_handler(state=Form1.binn)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['binn'] = message.text

    await Form1.next()
    await bot.send_message(message.from_user.id, "Выберите страну", reply_markup=nav.mark)
    # await list_categories(message)
  
    # await message.reply("Выберите страну")

# async def list_categories(message: types.Message, **kwargs):
#     mrk = await categories_country_keyboard()

# async def categories_country_keyboard():
#     mark = InlineKeyboardMarkup()
#     nn = BD1.all_country()
#     for i in nn:
#         button_text = f"{i}"
#         print(button_text)

#         mark.insert(
#             InlineKeyboardButton(text=button_text)
#         )
# # Проверяем возраст
# @dp.message_handler(lambda message: not message.text.isdigit(), state=Form.nameper)



# @dp.message_handler(state=Form1.nameper)
# async def process_name(message: types.Message, state: FSMContext, callback: types.CallbackQuery):
#     async with state.proxy() as data:
#         data['nameper'] = message.text

#     await Form1.next()
#     await callback.message.edit_reply_markup(nav.mark_blank_vid)
#     # await mark_blank_vid('Австрия')
#     await message.reply("Введите гос.номер или напиши /cancel")

# Сохраняем пол, выводим анкету
# @dp.message_handler(state=Form.gosnum)
# async def process_gender(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         global g_binn, g_nameper, g_gosnum
#         data['gosnum'] = message.text
#         markup = types.ReplyKeyboardRemove()

#         await bot.send_message(
#             message.chat.id,
#             md.text(
#                 md.text('БИН/ИИН: ', md.bold(data['binn'])),
#                 md.text('Наименование перевозчика:', md.code(data['nameper'])),
#                 md.text('Гос.номер:', data['gosnum']),
#                 sep='\n',
#             ),
#             reply_markup=markup,
#             parse_mode=ParseMode.MARKDOWN,
#         )
#         g_binn = data['binn']
#         g_nameper = data["nameper"]
#         g_gosnum = data["gosnum"]

#     await state.finish()
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Редактировать", "Сохранить", "Отмена"]
#     keyboard.add(*buttons)
#     await message.answer("Проверьте введеные данные", reply_markup=keyboard)




    # await message.reply(BD1.ss())
    # await bot.delete_message(message.from_user.id, message.message.message_id)
    # await bot.send_message(message.from_user.id, "Ввод информации по перевозчику", reply_markup=nav.menuInPer)
from aiogram.dispatcher.filters import Text

# @dp.message_handler(Text("Редактировать"))
# async def w_edit(message: types.Message):
#     await message.reply("Введите номер поля для редактирования", reply_markup=types.ReplyKeyboardRemove())

# @dp.message_handler(lambda message: message.text == "Сохранить")
# async def w_safe(message: types.Message):
#     BD1.ins(g_binn, g_nameper, g_gosnum)
#     await message.reply("Сохранено", reply_markup=types.ReplyKeyboardRemove())
#     await bot.send_message(message.from_user.id, "Главное меню", reply_markup=nav.menuInBlank)

# @dp.message_handler(lambda message: message.text == "Отмена")
# async def w_cancel(message: types.Message):
#     await message.reply("Возврат в главное меню", reply_markup=types.ReplyKeyboardRemove())
#     await bot.send_message(message.from_user.id, "Главное меню", reply_markup=nav.mainMenu)

# def register_handlers_start1(dp: Dispatcher):
#     dp.register_message_handler(start1, commands=['start1'])
