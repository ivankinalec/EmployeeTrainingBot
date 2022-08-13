from aiogram import Bot, Dispatcher, executor, types
import markups as navi
from db import Database

API_TOKEN = '5327530213:AAGPGVW4rzeyQkM16eh8WexkX7eqNqNneyo'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')


# КАБИНЕТ АДМИНИСТРАТОРА
# Список лекций по Excel
xlLecture1 = 'C:/Users/Aleksandr/PycharmProjects/EmployeeTrainerBot/Lec/Лекция 1.pdf'
#xlLecture2 = 'C:/Users/Aleksandr/PycharmProjects/EmployeeTrainerBot/Lec/Лекция 2.pdf'
#xlLecture3 = 'C:/Users/Aleksandr/PycharmProjects/EmployeeTrainerBot/Lec/Лекция 3.pdf'
# Список видеолекций по Excel
xlVideo1 = 'https://youtu.be/4roVtL2mynA'
#xlVideo2 =
#xlVideo3 =
# Список тестов по Excel
#xlTest1 =
#xlTest2 =
#xlTest3 =
# Список лекций по Яндекс Таблицам
#yndxLec1 =
#yndxLec2 =
#yndxLec3 =
# Список видеолекций по Яндекс Таблицам
#yndxVideo1 =
#yndxVideo2 =
#yndxVideo3 =
# Список тестов по Яндекс Таблицам
#yndxTest1 =
#yndxTest2 =
#yndxTest3 =


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    Расписать, что делает функция
    """
    await message.reply("Здравствуйте, коллега!\nНажмите на /login, чтобы зарегистрироваться.")


@dp.message_handler(commands='login')
async def login(message: types.Message):
    """
    Расписать, что делает функция
    """
    await bot.send_message(message.from_user.id, "Введите ваш табельный номер.")

@dp.message_handler()
async def check_login(message: types.Message):
    """
    Расписать, что делает функция
    """
    if db.does_he_work(message.text):
        first_name = db.hello(message.text)
        await bot.send_message(message.from_user.id, f"Добро пожаловать, {first_name[0]} {first_name[1]}! Выберите, какой программе вы хотите обучиться.", reply_markup=navi.mainMenu)

    elif message.text == 'Microsoft Excel':
        await bot.send_message(message.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    elif message.text == 'Яндекс Таблицы':
        await bot.send_message(message.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)
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
        await bot.send_message(call.from_user.id, 'Здесь должна быть лекция 2')
    # вызов третьей лекции по Excel:
    elif call.data == "eLec3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть лекция 3')
    # вызов кнопки назад
    elif call.data == "eBackLec":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    # -- МЕНЮ ВИДЕОЛЕКЦИИ --
    # вызов первой виделекции по Excel:
    elif call.data == "eVideo1":
        await bot.send_message(call.from_user.id, xlVideo1)
    # вызов второй лекции по Excel:
    elif call.data == "eVideo2":
        await bot.send_message(call.from_user.id, 'https://youtu.be/uULZ0VlvigY')
    # вызов третьей лекции по Excel:
    elif call.data == "eVideo3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть video 3')
    # вызов кнопки назад
    elif call.data == "eBackVideo":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineExcelKeyboard)

    # -- МЕНЮ ТЕСТОВ --
    # вызов первого теста по Excel:
    elif call.data == "eTest1":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 1')
    # вызов второго теста по Excel:
    elif call.data == "eTest2":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 2')
    # вызов третьего теста по Excel:
    elif call.data == "eTest3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 3')
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
        await bot.send_message(call.from_user.id, 'Здесь должна быть лекция 1')
    # вызов второй лекции по Yandex:
    elif call.data == "yLec2":
        await bot.send_message(call.from_user.id, 'Здесь должна быть лекция 2')
    # вызов третьей лекции по Yandex:
    elif call.data == "yLec3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть лекция 3')
    # вызов кнопки назад
    elif call.data == "yBackLec":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)

    # -- МЕНЮ ВИДЕОЛЕКЦИИ --
    # вызов первой виделекции по Yandex:
    elif call.data == "yVideo1":
        await bot.send_message(call.from_user.id, 'Здесь должна быть видео 1')
    # вызов второй лекции по Yandex:
    elif call.data == "yVideo2":
        await bot.send_message(call.from_user.id, 'Здесь должна быть video 2')
    # вызов третьей лекции по Yandex:
    elif call.data == "yVideo3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть video 3')
    # вызов кнопки назад
    elif call.data == "yBackVideo":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)

    # -- МЕНЮ ТЕСТОВ --
    # вызов первого теста по Yandex:
    elif call.data == "yTest1":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 1')
    # вызов второго теста по Yandex:
    elif call.data == "yTest2":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 2')
    # вызов третьего теста по Yandex:
    elif call.data == "yTest3":
        await bot.send_message(call.from_user.id, 'Здесь должна быть Test 3')
    # вызов кнопки назад
    elif call.data == "yBackTest":
        await bot.send_message(call.from_user.id, 'Выберите категорию:', reply_markup=navi.inlineYandexKeyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
