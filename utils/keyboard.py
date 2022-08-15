from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клаватуры
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
confirm.row(KeyboardButton('🖋Редактировать(not work)'))
confirm.row(KeyboardButton('❌Отмена'))

# Инлайн-клавиатуры

save_request = InlineKeyboardMarkup(row_width=2)
save_request.add(
    InlineKeyboardButton('Да', callback_data='yes_t'),
    InlineKeyboardButton('Нет',callback_data='no'),    
)

edit_message = InlineKeyboardMarkup(row_width=2)
edit_message.add(
    InlineKeyboardButton('Группа',callback_data='edit_group'),
    InlineKeyboardButton('Имя', callback_data='edit_name'),
    InlineKeyboardButton('Литраж',callback_data='edit_L'),
    InlineKeyboardButton('Количество',callback_data='edit_count')
)

