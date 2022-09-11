from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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

