import telebot
from openpyxl import load_workbook

keyboard1 = telebot.types.ReplyKeyboardMarkup(True,)
keyboard1.row('Сервера', 'Системы хранения данных')
keyboard1.row('Английский')

keyboardStorage = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage.row('All-Flash', 'Гибридные')
keyboardStorage.row('Назад')

keyboardStorageAllFlash = telebot.types.ReplyKeyboardMarkup(True,)
keyboardStorageAllFlash.row('OceanStor Dorado V3','OceanStor Dorado V6')
keyboardStorageAllFlash.row('Назад')

keyboardStorageDoradoV3 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV3.row('Брошура','Оф-документация')
keyboardStorageDoradoV3.row('Описание','Тесты')
keyboardStorageDoradoV3.row('3D модель')
keyboardStorageDoradoV3.row('Назад')

keyboardStorageDoradoV6 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV6.row('Назад')

keyboardStorageHybrid = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageHybrid.row('OceanStor 2200 V3','OceanStor 2600 V3')
keyboardStorageHybrid.row('OceanStor 5000 V5','OceanStor 6800 V5')
keyboardStorageHybrid.row('OceanStor 18000 V5')
keyboardStorageHybrid.row('Назад')

keyboardStorage2200 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2200.row('Описание','3D модель')
keyboardStorage2200.row('Назад')

keyboardStorage2600 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2600.row('Описание','Брошура')
keyboardStorage2600.row('3D модель')
keyboardStorage2600.row('Назад')

keyboardStorage5000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage5000.row('Описание','Брошура')
keyboardStorage5000.row('Оф-документация','3D модель')
keyboardStorage5000.row('Назад')

keyboardStorage6800 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage6800.row('Описание','Брошура')
keyboardStorage6800.row('Оф-документация','3D модель')
keyboardStorage6800.row('Назад')

keyboardStorage18000 = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage18000.row('Описание','Брошура')
keyboardStorage18000.row('Оф-документация','3D модель')
keyboardStorage18000.row('Назад')


#Open file with data
wb = load_workbook(filename='info.xlsx')
sheet_ranges = wb['storage_ru']


def russian(bot,message,type,i):

    if message.text.lower() == 'russian/русский' or message.text.lower() == 'russian':
        bot.send_message(message.chat.id,
                         'Привет, ' + message.from_user.first_name + ', вас приветствует HuaweiEBG_Bot ✋. Какое направление вас интересеут?',
                         reply_markup=keyboard1)

    elif message.text.lower() == 'системы хранения данных':
        bot.send_message(message.chat.id, 'Выберете тип системы хранения данных', reply_markup=keyboardStorage)

    elif message.text.lower() == 'all-flash':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageAllFlash)

    elif message.text.lower() == 'гибридные':
        bot.send_message(message.chat.id, 'Выберете интересующий модельный ряд', reply_markup=keyboardStorageHybrid)

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Какое направление вас интересеут?', reply_markup=keyboard1)

    elif message.text.lower() == 'oceanstor dorado v3':
        type[i] = 1
        bot.send_message(message.chat.id, sheet_ranges["C9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["C5"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'брошура' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 БРОШУРА 👇👇👇 \n' + sheet_ranges["C5"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'оф-документация' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + sheet_ranges["C7"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'описание' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["C8"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'тесты' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 ТЕСТЫ 👇👇👇 \n' + sheet_ranges["C6"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == '3d модель' and type[i] == 1:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["C6"].value,
                 reply_markup=keyboardStorageDoradoV3)

    elif message.text.lower() == 'oceanstor dorado v6':
        type[i] = 2
        bot.send_message(message.chat.id, sheet_ranges["B9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["B3"].value,
                 reply_markup=keyboardStorageDoradoV6)

    elif message.text.lower() == 'oceanstor 2200 v3':
        type[i] = 3
        bot.send_message(message.chat.id, sheet_ranges["D9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["D3"].value,
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == 'описание' and type[i] == 3:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["D8"].value,
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == '3d модель' and type[i] == 3:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["D4"].value,
                 reply_markup=keyboardStorage2200)

    elif message.text.lower() == 'oceanstor 2600 v3':
        type[i] = 4
        bot.send_message(message.chat.id, sheet_ranges["E9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["E3"].value,
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'описание' and type[i] == 4:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["E8"].value,
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'брошура' and type[i] == 4:
        bot.send_message(message.chat.id, '👇👇👇 БРОШУРА 👇👇👇 \n' + sheet_ranges["E5"].value,
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == '3d модель' and type[i] == 4:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["E4"].value,
                 reply_markup=keyboardStorage2600)

    elif message.text.lower() == 'oceanstor 5000 v5':
        type[i] = 5
        bot.send_message(message.chat.id, sheet_ranges["F9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["F3"].value,
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'оф-документация' and type[i] == 5:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + sheet_ranges["F7"].value,
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'описание' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["F8"].value,
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'брошура' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + sheet_ranges["F5"].value,
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == '3d модель' and type[i] == 5:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["F4"].value,
                 reply_markup=keyboardStorage5000)

    elif message.text.lower() == 'oceanstor 6800 v5':
        type[i] = 6
        bot.send_message(message.chat.id, sheet_ranges["G9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["G3"].value,
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'оф-документация' and type[i] == 6:
        bot.send_message(message.chat.id, '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + sheet_ranges["G7"].value,
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'описание' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["G8"].value,
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'брошура' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + sheet_ranges["G5"].value,
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == '3d модель' and type[i] == 6:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["G4"].value,
                 reply_markup=keyboardStorage6800)

    elif message.text.lower() == 'oceanstor 18000 v5':
        type[i] = 7
        bot.send_message(message.chat.id, sheet_ranges["H9"].value +
                 """\n\n Для ссылки на документацию, выберете интересующий документ
                 \n""" + sheet_ranges["H3"].value,
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'оф-документация' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 ДОКУМЕНТАЦИЯ 👇👇👇 \n' + sheet_ranges["H7"].value,
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'описание' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 ОПИСАНИЕ 👇👇👇 \n' + sheet_ranges["H8"].value,
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == 'брошура' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 БРОШУРА 👇👇👇 \n' + sheet_ranges["H6"].value,
                 reply_markup=keyboardStorage18000)

    elif message.text.lower() == '3d модель' and type[i] == 7:
        bot.send_message(message.chat.id,
                 '👇👇👇 3D МОДЕЛЬ 👇👇👇 \n' + sheet_ranges["H4"].value,
                 reply_markup=keyboardStorage18000)

    else:
        bot.send_message(message.chat.id,'Sorry, I do not understand you. Please click on the button or write /start')