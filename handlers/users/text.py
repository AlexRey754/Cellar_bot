from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states import Request_reg
import keyboards
from utils.db_api import db

@dp.message_handler(content_types=['text'])
async def text_buttons_func(message: types.Message, state: FSMContext):
    # uid = message.from_user.id
    if message.text == '➕Добавить позицию':
        await message.answer('К какой групе отнести позицию?', reply_markup=keyboards.default.groups)
        await Request_reg.group.set()

    elif message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)

    elif message.text == '🤚Взял(а)':
        pass

    elif message.text == '🗒Список':
        text = db.get_data()
        await message.answer(text)

    elif message.text == '⚙️Настройки':
        pass