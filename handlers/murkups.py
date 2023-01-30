
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

# mainMenu.insert(btnInPer)
# mainMenu.insert(btnInBlank)
# mainMenu.insert(btnInGruz)
# mainMenu.insert(btnOutPer)
# mainMenu.insert(btnOutBlank)
# mainMenu.insert(btnOutGruz)