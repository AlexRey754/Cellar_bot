from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states import Request_reg
import keyboards

@dp.callback_query_handler(text='edit_group')
async def edit_group_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('К какой групе отнести позицию?', reply_markup=keyboards.default.groups)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(group=callback_query.message.text)
        data = await state.get_data()
        state_group = data.get('group')
        state_name = data.get('name')
        state_L = data.get('L')
        state_count = data.get('count')
        text=f"""
        Группа: {state_group}
        Имя: {state_name}
        Литраж: {state_L}
        Количество: {state_count}
        """
        await callback_query.message.answer(text, reply_markup=keyboards.default.confirm)
    
@dp.callback_query_handler(text='edit_name')
async def edit_name_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новое имя: ', reply_markup=keyboards.default.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(name=callback_query.message.text)
        data = await state.get_data()
        state_group = data.get('group')
        state_name = data.get('name')
        state_L = data.get('L')
        state_count = data.get('count')
        text=f"""
        Группа: {state_group}
        Имя: {state_name}
        Литраж: {state_L}
        Количество: {state_count}
        """
        await callback_query.message.answer(text, reply_markup=keyboards.default.confirm)

@dp.callback_query_handler(text='edit_L')
async def edit_L_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новый литраж: ', reply_markup=keyboards.default.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(L=callback_query.message.text)
        data = await state.get_data()
        state_group = data.get('group')
        state_name = data.get('name')
        state_L = data.get('L')
        state_count = data.get('count')
        text=f"""
        Группа: {state_group}
        Имя: {state_name}
        Литраж: {state_L}
        Количество: {state_count}
        """
        await callback_query.message.answer(text, reply_markup=keyboards.default.confirm)

@dp.callback_query_handler(text='edit_count')
async def edit_count_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новое Количество: ', reply_markup=keyboards.default.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        await state.update_data(count=callback_query.message.text)
        data = await state.get_data()
        state_group = data.get('group')
        state_name = data.get('name')
        state_L = data.get('L')
        state_count = data.get('count')
        text=f"""
        Группа: {state_group}
        Имя: {state_name}
        Литраж: {state_L}
        Количество: {state_count}
        """
        await callback_query.message.answer(text, reply_markup=keyboards.default.confirm)