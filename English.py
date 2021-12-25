import telebot
from openpyxl import load_workbook

keyboardEN = telebot.types.ReplyKeyboardMarkup(True,)
keyboardEN.row('Servers', 'Storages')
keyboardEN.row('Russian')

keyboardStorageEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageEN.row('All-Flash', 'Hybrid')
keyboardStorageEN.row('Back')

keyboardStorageAllFlashEN = telebot.types.ReplyKeyboardMarkup(True,)
keyboardStorageAllFlashEN.row('OceanStor Dorado V3','OceanStor Dorado V6')
keyboardStorageAllFlashEN.row('Back')


keyboardStorageDoradoV3EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV3EN.row('Data Sheet','Documentations')
keyboardStorageDoradoV3EN.row('Description','Tests')
keyboardStorageDoradoV3EN.row('3D-model')
keyboardStorageDoradoV3EN.row('Back')


keyboardStorageDoradoV6EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageDoradoV6EN.row('Back')


keyboardStorageHybridEN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorageHybridEN.row('OceanStor 2200 V3','OceanStor 2600 V3')
keyboardStorageHybridEN.row('OceanStor 5000 V5','OceanStor 6800 V5')
keyboardStorageHybridEN.row('OceanStor 18000 V5')
keyboardStorageHybridEN.row('Back')

keyboardStorage2200EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2200EN.row('Description','3D-model')
keyboardStorage2200EN.row('Back')

keyboardStorage2600EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage2600EN.row('Description','Data Sheet')
keyboardStorage2600EN.row('3D-model')
keyboardStorage2600EN.row('Back')

keyboardStorage5000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage5000EN.row('Description','Data Sheet')
keyboardStorage5000EN.row('Documentations','3D-model')
keyboardStorage5000EN.row('Back')

keyboardStorage6800EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage6800EN.row('Description','Data Sheet')
keyboardStorage6800EN.row('Documentations','3D-model')
keyboardStorage6800EN.row('Back')

keyboardStorage18000EN = telebot.types.ReplyKeyboardMarkup(True)
keyboardStorage18000EN.row('Description','Data Sheet')
keyboardStorage18000EN.row('Documentations','3D-model')
keyboardStorage18000EN.row('Back')


#Open file with data
wb = load_workbook(filename='info.xlsx')
sheet_ranges = wb['storage_en']


def english(bot,message,type,i):

    if message.text.lower() == 'english/английский' or message.text.lower() == 'английский':
        bot.send_message(message.chat.id,
                     'Hello, ' + message.from_user.first_name + ', Welcome to HuaweiEBG_Bot ✋. Which direction are you interested in?',
                     reply_markup=keyboardEN)

    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, 'Which direction are you interested in?', reply_markup=keyboardEN)

    elif message.text.lower() == 'storages':
        bot.send_message(message.chat.id, 'Choose the type of storage system',reply_markup=keyboardStorageEN)

    elif message.text.lower() == 'all-flash':
        bot.send_message(message.chat.id, 'Choose the model range you are interested in', reply_markup=keyboardStorageAllFlashEN)
    elif message.text.lower() == 'hybrid':
        bot.send_message(message.chat.id, 'Choose the model range you are interested in', reply_markup=keyboardStorageHybridEN)

    elif message.text.lower() == 'oceanstor dorado v3':
        type[i] = 1
        bot.send_message(message.chat.id, sheet_ranges["C9"].value +
        """\n\n For a link to the documentation, select the document of interest
        \n""" + sheet_ranges["C3"].value,
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'data sheet' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Data Sheet 👇👇👇 \n' + sheet_ranges["C5"].value,
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'documentations' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + sheet_ranges["C7"].value,
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'description' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["C8"].value,
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == 'tests' and type[i] == 1:
        bot.send_message(message.chat.id, '👇👇👇 Tests 👇👇👇 \n' + sheet_ranges["C9"].value,
                         reply_markup=keyboardStorageDoradoV3EN)
    elif message.text.lower() == '3d-model' and type[i] == 1:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["C4"].value,
                         reply_markup=keyboardStorageDoradoV3EN)

    elif message.text.lower() == 'oceanstor dorado v6':
        type[i] = 2
        bot.send_message(message.chat.id, sheet_ranges["B9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["B3"].value,
                         reply_markup=keyboardStorageDoradoV6EN)

    elif message.text.lower() == 'oceanstor 2200 v3':
        type[i] = 3
        bot.send_message(message.chat.id, sheet_ranges["D9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["D3"].value,
                         reply_markup=keyboardStorage2200EN)
    elif message.text.lower() == 'description' and type[i] == 3:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["D8"].value,
                         reply_markup=keyboardStorage2200EN)
    elif message.text.lower() == '3d-model' and type[i] == 3:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["D4"].value,
                         reply_markup=keyboardStorage2200EN)

    elif message.text.lower() == 'oceanstor 2600 v3':
        type[i] = 4
        bot.send_message(message.chat.id, sheet_ranges["E9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["E3"].value,
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == 'description' and type[i] == 4:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["E8"].value,
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == 'data sheet' and type[i] == 4:
        bot.send_message(message.chat.id, '👇👇👇 Data Sheet 👇👇👇 \n' + sheet_ranges["E5"].value,
                         reply_markup=keyboardStorage2600EN)
    elif message.text.lower() == '3d-model' and type[i] == 4:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["E4"].value,
                         reply_markup=keyboardStorage2600EN)

    elif message.text.lower() == 'oceanstor 5000 v5':
        type[i] = 5
        bot.send_message(message.chat.id, sheet_ranges["F9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["F3"].value,
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'documentations' and type[i] == 5:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + sheet_ranges["F7"].value,
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'description' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["F8"].value,
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + sheet_ranges["F5"].value,
                         reply_markup=keyboardStorage5000EN)
    elif message.text.lower() == '3d-model' and type[i] == 5:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["F4"].value,
                         reply_markup=keyboardStorage5000EN)

    elif message.text.lower() == 'oceanstor 6800 v5':
        type[i] = 6
        bot.send_message(message.chat.id, sheet_ranges["G9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["G3"].value,
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'documentations' and type[i] == 6:
        bot.send_message(message.chat.id, '👇👇👇 Documentations 👇👇👇 \n' + sheet_ranges["G7"].value,
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'description' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["G8"].value,
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == 'data sheet' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + sheet_ranges["G5"].value,
                         reply_markup=keyboardStorage6800EN)
    elif message.text.lower() == '3d-model' and type[i] == 6:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["G4"].value,
                         reply_markup=keyboardStorage6800EN)

    elif message.text.lower() == 'oceanstor 18000 v5':
        type[i] = 7
        bot.send_message(message.chat.id, sheet_ranges["H9"].value +
                         """\n\n For a link to the documentation, select the document of interest
                         \n""" + sheet_ranges["H3"].value,
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'documentations' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Documentations 👇👇👇 \n' + sheet_ranges["H7"].value,
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'description' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Description 👇👇👇 \n' + sheet_ranges["H8"].value,
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == 'data sheet' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 Data Sheet 👇👇👇 \n' + sheet_ranges["H5"].value,
                         reply_markup=keyboardStorage18000EN)
    elif message.text.lower() == '3d-model' and type[i] == 7:
        bot.send_message(message.chat.id,
                         '👇👇👇 3D-model 👇👇👇 \n' + sheet_ranges["H4"].value,
                         reply_markup=keyboardStorage18000EN)

    else:
        bot.send_message(message.chat.id,'Sorry, I do not understand you. Please click on the button or write /start')