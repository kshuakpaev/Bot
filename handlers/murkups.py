
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .bdd import BD1
# import main
# import unitss

# Главное меню
mainMenu = InlineKeyboardMarkup(row_width=2)
btnInPer = InlineKeyboardButton(text="Ввод перевозчика", callback_data="btnInPer")
btnInBlank = InlineKeyboardButton(text="Разместить бланк разрешения", callback_data="btnInBlank")
btnInGruz = InlineKeyboardButton(text="Ввод грузоотправителя", callback_data="btnInGruz")
btnOutPer = InlineKeyboardButton(text="Поиск перевозчика", callback_data="btnOutPer")
btnOutBlank = InlineKeyboardButton(text="Поиск бланка разрешения", callback_data="btnOutBlank")
btnOutGruz = InlineKeyboardButton(text="Поиск грузоотправителя", callback_data="btnOutGruz")

mainMenu.insert(btnInPer)
mainMenu.insert(btnInBlank)
mainMenu.insert(btnInGruz)
mainMenu.insert(btnOutPer)
mainMenu.insert(btnOutBlank)
mainMenu.insert(btnOutGruz)

# Ввод информации по перевозчику
menuInPer = InlineKeyboardMarkup(row_width=2)
btnMainMenu = InlineKeyboardButton(text="Главное меню", callback_data="btnMainMenu")
btnVInPer = InlineKeyboardButton(text="Ввод информации по перевозчику", callback_data="btnVInPer")

menuInPer.insert(btnVInPer)
menuInPer.insert(btnMainMenu)

# Размещение бланка разрешения
menuInBlank = InlineKeyboardMarkup(row_width=2)
btnMainMenu = InlineKeyboardButton(text="Главное меню", callback_data="btnMainMenu")
btnVInBlank = InlineKeyboardButton(text="Разместить бланк разрешения", callback_data="btnVInBlank")

# menuInPer.insert(btnVInPer)
menuInBlank.insert(btnVInBlank)
menuInBlank.insert(btnMainMenu)


mark = InlineKeyboardMarkup(row_width=3)
nn = BD1.all_country()
for i in nn:
    button_text = f"{i}"
    # print(button_text)
    mark.insert(
        InlineKeyboardButton(text=button_text, callback_data=button_text)
    )

async def mark_blank_vid(country):
    mark_blank = InlineKeyboardMarkup(row_width=3)
    nn = BD1.blank_country(country)
    for i in nn:
        button_text = f"{i}"
    # print(button_text)
    mark_blank.insert(
        InlineKeyboardButton(text=button_text, callback_data=button_text)
    )

# nn = BD1.all_country()
# ptt = []
# for i in nn:
#     ss = ""
#     ss = i
#     ptt[i] = ss
#     print(ss.strip())
#     print(ptt[i])

# mainMenu.insert(btnInPer)
# mainMenu.insert(btnInBlank)
# mainMenu.insert(btnInGruz)
# mainMenu.insert(btnOutPer)
# mainMenu.insert(btnOutBlank)
# mainMenu.insert(btnOutGruz)