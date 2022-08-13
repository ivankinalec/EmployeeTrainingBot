from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# ГЛАВНОЕ МЕНЮ
btnExcel = KeyboardButton('Microsoft Excel')
btnYandex = KeyboardButton('Яндекс Таблицы')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnExcel, btnYandex)



# МЕНЮ ДЛЯ EXCEL
inlineExcelKeyboard = InlineKeyboardMarkup(row_width=3)
btnELec = InlineKeyboardButton('Лекции', callback_data='eLec')
btnEVideo = InlineKeyboardButton('Видеолекции', callback_data='eVideo')
btnETest = InlineKeyboardButton('Тесты', callback_data='eTest')
inlineExcelKeyboard.add(btnELec, btnEVideo, btnETest)

# Меню для лекций по Excel
excelLec = InlineKeyboardMarkup(row_width=3)
excelLec1 = InlineKeyboardButton('Лекция 1', callback_data='eLec1')
excelLec2 = InlineKeyboardButton('Лекция 2', callback_data='eLec2')
excelLec3 = InlineKeyboardButton("Лекция 3", callback_data='eLec3')
excelBackLec = InlineKeyboardButton("Назад", callback_data='eBackLec')
excelLec.add(excelLec1, excelLec2, excelLec3, excelBackLec)

# Меню для видеолекций по Excel
excelVideo = InlineKeyboardMarkup()
excelVideo1 = InlineKeyboardButton('Видео 1', callback_data='eVideo1')
excelVideo2 = InlineKeyboardButton('Видео 2', callback_data='eVideo2')
excelVideo3 = InlineKeyboardButton("Видео 3", callback_data='eVideo3')
excelBackVideo = InlineKeyboardButton("Назад", callback_data='eBackVideo')
excelVideo.add(excelVideo1, excelVideo2, excelVideo3, excelBackVideo)

# Меню для тестов по Excel
excelTest = InlineKeyboardMarkup(row_width=3)
excelTest1 = InlineKeyboardButton('Тест 1', callback_data='eTest1')
excelTest2 = InlineKeyboardButton('Тест 2', callback_data='eTest2')
excelTest3 = InlineKeyboardButton("Тест 3", callback_data='eTest3')
excelBackTest = InlineKeyboardButton("Назад", callback_data='eBackTest')
excelTest.add(excelTest1, excelTest2, excelTest3, excelBackTest)



# МЕНЮ ДЛЯ YANDEX
inlineYandexKeyboard = InlineKeyboardMarkup(row_width=3)
btnYLec = InlineKeyboardButton('Лекции', callback_data='yLec')
btnYVideo = InlineKeyboardButton('Видеолекции', callback_data='yVideo')
btnYTest = InlineKeyboardButton('Тесты', callback_data='yTest')
#btnYBack = InlineKeyboardButton('Назад', callback_data='yBack')
inlineYandexKeyboard.add(btnYLec, btnYVideo, btnYTest)

# Меню для лекций по Yandex
yandexLec = InlineKeyboardMarkup(row_width=3)
yandexLec1 = InlineKeyboardButton('Лекция 1', callback_data='yLec1')
yandexLec2 = InlineKeyboardButton('Лекция 2', callback_data='yLec2')
yandexLec3 = InlineKeyboardButton("Лекция 3", callback_data='yLec3')
yandexBackLec = InlineKeyboardButton("Назад", callback_data='yBackLec')
yandexLec.add(yandexLec1, yandexLec2, yandexLec3, yandexBackLec)

# Меню для видеолекций по Yandex
yandexVideo = InlineKeyboardMarkup()
yandexVideo1 = InlineKeyboardButton('Видео 1', callback_data='yVideo1')
yandexVideo2 = InlineKeyboardButton('Видео 2', callback_data='yVideo2')
yandexVideo3 = InlineKeyboardButton("Видео 3", callback_data='yVideo3')
yandexBackVideo = InlineKeyboardButton("Назад", callback_data='yBackVideo')
yandexVideo.add(yandexVideo1, yandexVideo2, yandexVideo3, yandexBackVideo)

# Меню для тестов по Yandex
yandexTest = InlineKeyboardMarkup(row_width=3)
yandexTest1 = InlineKeyboardButton('Тест 1', callback_data='yTest1')
yandexTest2 = InlineKeyboardButton('Тест 2', callback_data='yTest2')
yandexTest3 = InlineKeyboardButton("Тест 3", callback_data='yTest3')
yandexBackTest = InlineKeyboardButton("Назад", callback_data='yBackTest')
yandexTest.add(yandexTest1, yandexTest2, yandexTest3, yandexBackTest)
