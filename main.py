
import asyncio
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from config import TOKEN

from utils import db
from utils import keyboard
from utils.settings import Request_reg

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode='html')
storage = MemoryStorage()  # для стейтов
dp = Dispatcher(bot, loop=loop, storage=storage)

logging.basicConfig(level=logging.INFO)  # ЛОГИРОВАНИЕ


@dp.message_handler(commands=['start'], state=None)
async def start_mes(message):
    uid = message.from_user.id
    await bot.send_message(uid,"Some text",reply_markup=keyboard.menu)

#---------------[TEST]---------------\

@dp.message_handler(commands=['a'], state=None)
async def testing_features(message):
    """"
    TODO: DELETE IN  FUTURE
    """
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    from utils import keyboard
    print(keyboard.save_request)   
    await message.answer('TEST',reply_markup=keyboard.save_request)

@dp.callback_query_handler(text='yes_t')
async def edit_group_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer("YE{P")
    try:
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
        await callback_query.message.answer(text)
    except:
        await callback_query.message.answer("None") 
#---------------[TEST]---------------/

@dp.message_handler(content_types=['text'])
async def text_buttons_func(message: types.Message, state: FSMContext):
    uid = message.from_user.id
    if message.text == '➕Добавить позицию':
        await message.answer('К какой групе отнести позицию?', reply_markup=keyboard.groups)
        await Request_reg.group.set()

    elif message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboard.menu)

    elif message.text == '🤚Взял(а)':
        pass

    elif message.text == '🗒Список':
        text = db.get_all()
        message.answer(text)

    elif message.text == '⚙️Настройки':
        pass

# Стейты-----------------------------------\
@dp.message_handler(state=Request_reg.group)
async def reg_group(message: types.Message, state: FSMContext):
    text = message.text
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboard.menu)
    else:
        await state.update_data(group=text)
        await message.answer('Как назовёте позицию?',reply_markup=keyboard.cancel)
        await Request_reg.name.set()

@dp.message_handler(state=Request_reg.name)
async def reg_name(message: types.Message, state: FSMContext):
    text = message.text
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboard.menu)
    else:
        await state.update_data(name=text)
        await message.answer('Объём?',reply_markup=keyboard.cancel)
        await Request_reg.L.set()
    
@dp.message_handler(state=Request_reg.L)
async def reg_L(message: types.Message, state: FSMContext):

    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboard.menu)
    else:
        try:
            text = int(message.text)
            await state.update_data(L=text)
            await message.answer('Количество?',reply_markup=keyboard.cancel)
            await Request_reg.count.set()
        except:
            await message.answer("Нужно было ввести число! Введите еще раз!")
        
@dp.message_handler(state=Request_reg.count)
async def reg_count(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboard.menu)
    else:
        try:
            count=int(message.text)
            await state.update_data(count=count)
            data = await state.get_data()
            state_group = data.get('group')
            state_name = data.get('name')
            state_L = data.get('L')
            text=f"""
            Save yout request?
            """
            await message.answer(text, reply_markup=keyboard.confirm)
            await Request_reg.next()
        except TypeError as e:
            print(e)
            await message.answer("Нужно было ввести число! Введите еще раз!")
#------------------------------------------/


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
        db.add(name=state_name,L=state_L,count=state_count,group=state_group)
        await message.answer('Сохранил',reply_markup=keyboard.menu)

    elif message.text == '❎Нет':
        await message.answer('Запрос сброшен',reply_markup=keyboard.menu)
        await state.finish()
    
    elif message.text == '🖋Редактировать':
        await message.answer('Что вы хотите отредактировать?',reply_markup=keyboard.edit_message)

# #---------------[РЕДАКТИРОВАНИЕ]---------------\

@dp.callback_query_handler(text='edit_group')
async def edit_group_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('К какой групе отнести позицию?', reply_markup=keyboard.groups)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboard.menu)
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
        await callback_query.message.answer(text, reply_markup=keyboard.confirm)
    
@dp.callback_query_handler(text='edit_name')
async def edit_name_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новое имя: ', reply_markup=keyboard.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboard.menu)
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
        await callback_query.message.answer(text, reply_markup=keyboard.confirm)

@dp.callback_query_handler(text='edit_L')
async def edit_L_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новый литраж: ', reply_markup=keyboard.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboard.menu)
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
        await callback_query.message.answer(text, reply_markup=keyboard.confirm)

@dp.callback_query_handler(text='edit_count')
async def edit_count_request(callback_query: types.CallbackQuery,state: FSMContext):
    await callback_query.message.answer('Введите новое Количество: ', reply_markup=keyboard.cancel)
    if callback_query.message.text == '❌Отмена':
        await state.finish()
        await callback_query.message.answer('Отмена',reply_markup=keyboard.menu)
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
        await callback_query.message.answer(text, reply_markup=keyboard.confirm)
# #---------------[РЕДАКТИРОВАНИЕ]---------------/



if __name__== '__main__':
    print('--------------------------------------------------')
    db.init()
    try:
        executor.start_polling(dp,skip_updates=True)
    except Exception as e:
        print(e)
