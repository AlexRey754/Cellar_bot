from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states import Request_reg
from utils.db_api import db
import keyboards

@dp.message_handler(state=Request_reg.group)
async def reg_group(message: types.Message, state: FSMContext):
    text = message.text
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(group=text)
        await message.answer('Как назовёте позицию?',reply_markup=keyboards.default.cancel)
        await Request_reg.name.set()

@dp.message_handler(state=Request_reg.name)
async def reg_name(message: types.Message, state: FSMContext):
    text = message.text
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(name=text)
        await message.answer('Объём?',reply_markup=keyboards.default.cancel)
        await Request_reg.L.set()
    
@dp.message_handler(state=Request_reg.L)
async def reg_L(message: types.Message, state: FSMContext):

    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        try:
            text = int(message.text)
            await state.update_data(L=text)
            await message.answer('Количество?',reply_markup=keyboards.default.cancel)
            await Request_reg.count.set()
        except:
            await message.answer("Нужно было ввести число! Введите еще раз!")
        
@dp.message_handler(state=Request_reg.count)
async def reg_count(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        try:
            count=int(message.text)
            await state.update_data(count=count)
            data = await state.get_data()
            state_group = data.get('group')
            state_name = data.get('name')
            state_L = data.get('L')

            text=f"""Группа: {state_group}\nИмя: {state_name}\nЛитраж: {state_L}\nКоличество: {count}\n\nSave yout request?
            """
            await message.answer(text, reply_markup=keyboards.default.confirm)
            await Request_reg.next()
        except TypeError as e:
            print(e)
            await message.answer("Нужно было ввести число! Введите еще раз!")

@dp.message_handler(state=Request_reg._confirm)
async def yes_confirm_request(message: types.Message, state: FSMContext):
    """
    TODO:change request text
    """
    if message.text == '✅Да':
        data = await state.get_data()
        state_group = data.get('group')
        state_name = data.get('name')
        state_L = data.get('L')
        state_count = data.get('count')    
        db.add_request(group=state_group,name=state_name,Litres=state_L,count=state_count)
        
        await state.finish()
        await message.answer('Сохранил',reply_markup=keyboards.default.menu)


    elif message.text == '❎Нет':
        await message.answer('Запрос сброшен',reply_markup=keyboards.default.menu)
        await state.finish()
    
    elif message.text == '🖋Редактировать':
        await message.answer('Что вы хотите отредактировать?',reply_markup=keyboards.inline.edit_message)