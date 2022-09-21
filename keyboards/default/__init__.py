from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(True,True)
menu.row(KeyboardButton('➕Добавить позицию'))
menu.row(KeyboardButton('🤚Взял(а)'))
menu.row(KeyboardButton('🗒Список'))
menu.row(KeyboardButton('⚙️Настройки'))

groups = ReplyKeyboardMarkup(True,True)
groups.row(KeyboardButton('Соленья'))
groups.row(KeyboardButton('Компоты'))
groups.row(KeyboardButton('Варенье'))
groups.row(KeyboardButton('❌Отмена'))

cancel = ReplyKeyboardMarkup(True, True)
cancel.row(KeyboardButton('❌Отмена'))

confirm = ReplyKeyboardMarkup(True, True)
confirm.row(KeyboardButton('✅Да'),KeyboardButton('❎Нет'))
confirm.row(KeyboardButton('🖋Редактировать'))

