from aiogram import Bot, Dispatcher, executor, types
import markups as navi
from db import Database

API_TOKEN = 'TELEGRAM_API_TOKEN'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')



# Список лекций по Excel
xlLecture1 = 'path or url on Lecture 1'
xlLecture2 = 'path or url on Lecture 2'
xlLecture3 = 'path or url on Lecture 3'

# Список видеолекций по Excel
xlVideo1 = 'path or url on Video 1'
xlVideo2 = 'path or url on Video 2'
xlVideo3 = 'path or url on Video 3'

# Список тестов по Excel
xlTest1 = 'path or url on Test 1'
xlTest2 = 'path or url on Test 2'
xlTest3 = 'path or url on Test 3'

# Список лекций по Яндекс Таблицам
yndxLec1 = 'path or url on Lecture 1'
yndxLec2 = 'path or url on Lecture 2'
yndxLec3 = 'path or url on Lecture 3'

# Список видеолекций по Яндекс Таблицам
yndxVideo1 = 'path or url on Video 1'
yndxVideo2 = 'path or url on Video 2'
yndxVideo3 = 'path or url on Video 3'

# Список тестов по Яндекс Таблицам
yndxTest1 = 'path or url on Test 1'
yndxTest2 = 'path or url on Test 2'
yndxTest3 = 'path or url on Test 3'

# Обработка команды \start
@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте, коллега!\nНажмите на /login, чтобы зарегистрироваться.")

# Обработка команды \login
@dp.message_handler(commands='login')
async def login(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите ваш табельный номер.")

@dp.message_handler()
async def check_login(message: types.Message):
    if db.does_he_work(message.text):
        first_name = db.hello(message.text)
        await bot.send_message(message.from_user.id, f"Добро пожаловать, {first_name[0]} {first_name[1]}! Выберите, какой программе вы хотите обучиться.", reply_markup=navi.mainMenu)

    elif message.text == 'Microsoft Excel':
        await bot.send_message(message.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    elif message.text == 'Яндекс Таблицы':
        await bot.send_message(message.from_user.id, 'Обучение по данной программе находится в разработке', reply_markup=navi.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Кажется, вы у нас не работаете.")


@dp.callback_query_handler()
async def secondLevelMenu(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    # ВЫЗОВ МЕНЮ ЛЕКЦИЙ ПО EXCEL
    if call.data == "eLec":
        await bot.send_message(call.from_user.id, 'Выберите лекцию:', reply_markup=navi.excelLec)
    # ВЫЗОВ МЕНЮ ВИДЕОЛЕКЦИЙ ПО EXCEL
    elif call.data == "eVideo":
        await bot.send_message(call.from_user.id, 'Выберите видеолекцию:', reply_markup=navi.excelVideo)
    # ВЫЗОВ МЕНЮ ТЕСТОВ ПО EXCEL
    elif call.data == "eTest":
        await bot.send_message(call.from_user.id, 'Выберите тест:', reply_markup=navi.excelTest)

    # -- МЕНЮ ЛЕКЦИИ --
    # вызов первой лекции по Excel:
    elif call.data == "eLec1":
        lec1 = open(xlLecture1, 'rb')
        await bot.send_document(call.from_user.id, lec1)
    # вызов второй лекции по Excel:
    elif call.data == "eLec2":
        lec2 = open(xlLecture2, 'rb')
        await bot.send_message(call.from_user.id, lec2)
    # вызов третьей лекции по Excel:
    elif call.data == "eLec3":
        lec3 = open(xlLecture3, 'rb')
        await bot.send_message(call.from_user.id, lec3)
    # вызов кнопки назад
    elif call.data == "eBackLec":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    # -- МЕНЮ ВИДЕОЛЕКЦИИ --
    # вызов первой виделекции по Excel:
    elif call.data == "eVideo1":
        await bot.send_message(call.from_user.id, xlVideo1)
    # вызов второй лекции по Excel:
    elif call.data == "eVideo2":
        await bot.send_message(call.from_user.id, xlVideo2)
    # вызов третьей лекции по Excel:
    elif call.data == "eVideo3":
        await bot.send_message(call.from_user.id, xlVideo3)
    # вызов кнопки назад
    elif call.data == "eBackVideo":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    # -- МЕНЮ ТЕСТОВ --
    # вызов первого теста по Excel:
    elif call.data == "eTest1":
        await bot.send_message(call.from_user.id, xlTest1)
    # вызов второго теста по Excel:
    elif call.data == "eTest2":
        await bot.send_message(call.from_user.id, xlTest2)
    # вызов третьего теста по Excel:
    elif call.data == "eTest3":
        await bot.send_message(call.from_user.id, xlTest3)
    # вызов кнопки назад
    elif call.data == "eBackTest":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    # ВЫЗОВ МЕНЮ ЛЕКЦИЙ ПО YANDEX
    if call.data == "yLec":
        await bot.send_message(call.from_user.id, 'Выберите лекцию:', reply_markup=navi.yandexLec)
    # ВЫЗОВ МЕНЮ ВИДЕОЛЕКЦИЙ ПО YANDEX
    elif call.data == "yVideo":
        await bot.send_message(call.from_user.id, 'Выберите видеолекцию:', reply_markup=navi.yandexVideo)
    # ВЫЗОВ МЕНЮ ТЕСТОВ ПО YANDEX
    elif call.data == "yTest":
        await bot.send_message(call.from_user.id, 'Выберите тест:', reply_markup=navi.yandexTest)

    # -- МЕНЮ ЛЕКЦИИ --
    # вызов первой лекции по Yandex:
    elif call.data == "yLec1":
        await bot.send_message(call.from_user.id, yndxLec1)
    # вызов второй лекции по Yandex:
    elif call.data == "yLec2":
        await bot.send_message(call.from_user.id, yndxLec2)
    # вызов третьей лекции по Yandex:
    elif call.data == "yLec3":
        await bot.send_message(call.from_user.id, yndxLec3)
    # вызов кнопки назад
    elif call.data == "yBackLec":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)

    # -- МЕНЮ ВИДЕОЛЕКЦИИ --
    # вызов первой видеолекции по Yandex:
    elif call.data == "yVideo1":
        await bot.send_message(call.from_user.id, yndxVideo1)
    # вызов второй видеолекции по Yandex:
    elif call.data == "yVideo2":
        await bot.send_message(call.from_user.id, yndxVideo2)
    # вызов третьей видеолекции по Yandex:
    elif call.data == "yVideo3":
        await bot.send_message(call.from_user.id, yndxVideo3)
    # вызов кнопки назад
    elif call.data == "yBackVideo":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)

    # -- МЕНЮ ТЕСТОВ --
    # вызов первого теста по Yandex:
    elif call.data == "yTest1":
        await bot.send_message(call.from_user.id, yndxTest1)
    # вызов второго теста по Yandex:
    elif call.data == "yTest2":
        await bot.send_message(call.from_user.id, yndxTest2)
    # вызов третьего теста по Yandex:
    elif call.data == "yTest3":
        await bot.send_message(call.from_user.id, yndxTest3)
    # вызов кнопки назад
    elif call.data == "yBackTest":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
